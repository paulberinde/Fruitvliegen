# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:10:49 2016

@authors: Merel van den Hurk, Paul Berinde-Tâmpănariu, Jaap Nieuwenhuizen
"""

# import
import random
import itertools
import Queue
import copy

solved = False

class Node(object):
    def __init__(self, steps, genes, state, goal, parent, divisor):
        self.steps = steps
        self.genes = genes
        self.state = state
        self.tried = False
        self.misplaces = self.get_misplaces()
        self.misplaces_sum = sum(map(abs, self.misplaces)) * 100 / divisor
        self.getPatterns()
        if goal == 0:
            self.score = self.steps + (24 - self.pattern)
        elif goal == 1:
            self.score = self.genes + self.misplaces_sum
        self.parent = parent

    def get_misplaces(self):
        misplaces = []
        for gene in self.state:
            misplaces.append((gene - 1) - (self.state).index(gene))
        return misplaces

    def getPatterns(self):
        self.pattern = 0
        for index in range(0, 24):
            if ((self.state[index] == self.state[index + 1] + 1) or (self.state[index] == self.state[index + 1] - 1)):
                self.pattern += 1

    def createChildren(self, combinations, goal, divisor, priority_queue, archive):
        global solved
        self.tried = True
        for interval in combinations:
            # calculate necessary values
            child_steps = self.steps + 1
            child_genes = self.genes + (interval[1] - interval[0] + 1)

            # create new state
            child_state = copy.deepcopy(self.state)
            first_index = interval[0]
            second_index = interval[1]
            child_state[first_index:second_index + 1] = child_state[first_index:second_index + 1][::-1]

            # make child
            child = Node(child_steps, child_genes, child_state, goal, self, divisor)

            # check for solution and break if necessary
            if child.misplaces_sum == 0:
                solved = True
                archive.append(child)
                break
            else:
                solved = False

            # check for existing configurations based on goal
            # MAKE SURE THESE ARE EQUAL
            arch_exist = False
            arch_steps = None
            # check in archive
            archive.reverse()
            for node in archive:
                if child_state == node.state:
                    arch_exist = True
                    arch_steps = node.steps
                    break
            archive.reverse()
            # check in priority queue
            for entry in priority_queue.queue:
                if child_state == entry[1].state:
                    if child_steps < entry[1].steps:
                        # make child and archive old node
                        priority_queue.put((child.score, child))
                        archive.append(entry[1])
                        priority_queue.queue.remove(entry)
                else:
                    if arch_exist == True:
                        if child_steps < arch_steps:
                            priority_queue.put((child.score, child))
                    else:
                        priority_queue.put((child.score, child))
                break

        # move self to archive to finalize
        print "Archive length before pop: ", len(archive)
        print "Priority queue length before pop: ", len(priority_queue.queue)
        archive.append(self)
        priority_queue.get(self)
        print "Archive length after pop: ", len(archive)
        print "Priority queue length after pop: ", len(priority_queue.queue)
        return archive, priority_queue, solved


def runProgram(goal, genome):
    """
    Initialize case-specific variables based on user input
    Goal:
        0 = minimise number of inversions
        1 = minimise number of inverted genes
    Genome:
        0 = melanogaster
        1 = random
    """
    if goal == 0:
        divisor = 100
    elif goal == 1:
        divisor = 100
    if genome == 0:
        initial_genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    elif genome == 1:
        initial_genome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        random.shuffle(initial_genome)

    # initialize priority_queue
    priority_queue = Queue.PriorityQueue()
    print "Priority queue initialized."

    # initialize archive
    archive = []
    print "Archive initialized."

    # initialize itertools combinations
    combinations = []
    comb_len = 2
    for subset in itertools.combinations(range(0, 25), comb_len):
        combinations.append(subset)
    print "Combinations initialized."

    # set up first Node
    first_node = Node(0, 0, initial_genome, goal, None, divisor)
    first_node.tried = True
    print "First node set up."

    # add first node to priority queue
    priority_queue.put((first_node.score, first_node))
    print "First node pushed to priority queue."

    # create children
    first_node.createChildren(combinations, goal, divisor, priority_queue, archive)
    print "First node's children created."

    # repeat pathfinding until done
    while solved == False:
        # find node with lowest score in priority_queue and expand node
        print "Checkpoint"
        new_parent = priority_queue.get()
        print "PARENT INFORMATION:"
        print "Current step: ", new_parent[1].steps
        print "Current genes: ", new_parent[1].genes
        print "Current state: ", new_parent[1].state
        print new_parent[1].misplaces
        print "Current misplaces: ", new_parent[1].misplaces_sum
        print "Current score: ", new_parent[1].score
        # input("Press enter before creating new children...")
        new_parent[1].createChildren(combinations, goal, divisor, priority_queue, archive)

    # solution reached!
    print "Done!"
    for item in archive:
        if item.state == range(1, 26):
            print "Steps: ", item.steps, "\n"
            print "Genes transferred: ", item.genes, "\n", "\n"
            print "Solution: ", item.state, "\n"
            while item.parent != None:
                print "Previous: ", (item.parent).state, "\n"
                item.parent = (item.parent).parent
    '''
    for item in archive:
        print item.steps
        print item.state
    print "Done!"
    '''

# define user interface
user_goal = input('Press 0 for minimum amount of inversions and 1 for minimum amount of inverted genes: ')
user_genome = input('Press 0 for D. melanogaster genome and 1 for random genome: ')
runProgram(user_goal, user_genome)

input('You have reached a solution! Press anything to close the program.')
