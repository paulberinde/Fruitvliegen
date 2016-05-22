# Import
import random
import itertools
import Queue

# Node for storing a genome configuration.
class Node(object):
    def __init__(self, steps, genes, state, goal, parent, divisor):
        self.steps = steps
        self.genes = genes
        self.state = state
        self.getMisplaces()
        self.misplacesSum = sum(map(abs, self.misplaces)) / divisor
        if goal == 0:
            self.score = self.steps + self.misplacesSum
        elif goal == 1:
            self.score = self.genes + self.misplacesSum
        self.parent = parent

    def getMisplaces(self):
        self.misplaces = []
        for gene in self.state:
            (self.misplaces).append((gene - 1) - (self.state).index(gene))

    def createChildren(self, combinations, goal, divisor, priority_queue, archive):
        # PRINT CURRENT SELF
        print "Self: ", self.state
        for interval in combinations:
            # create new state
            child_state = self.state
            first_index = interval[0]
            second_index = interval[1]
            child_state[first_index:second_index + 1] = child_state[first_index:second_index + 1][::-1]
            
            # calculate new stepcount and gene-transfer values
            child_steps = self.steps + 1
            child_genes = self.genes + (interval[1] - interval[0] + 1)
            
            # create new child with calculated values
            child = Node(child_steps, child_genes, child_state, goal, self, divisor)
            
            # check if solution is reached
            if child.misplacesSum == 0:
                solved = True
                archive.append(child)
            else:
                solved = False
                priority_queue.put((child.score, child))
        
        # move self to archive to finalize
        archive.append(self)
        priority_queue.get((self.score, self))
        return archive, priority_queue, solved

def runProgram(goal, genome):
    '''
    Initialize case-specific variables based on user input
    Goal:
        0 = minimise number of inversions
        1 = minimise number of inverted genes
    Genome:
        0 = melanogaster
        1 = random
    '''
    if goal == 0:
        divisor = 1
    elif goal == 1:
        divisor = 1
    if genome == 0:
        initial_genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    elif genome == 1:
        initial_genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
        random.shuffle(initial_genome)

    # initialize priority_queue and archive
    priority_queue = Queue.PriorityQueue()
    archive = []

    # initialize itertools combinations
    combinations = []
    comb_len = 2
    for subset in itertools.combinations(range(0, 25), comb_len):
        combinations.append(subset)

    # set up first Node
    first_node = Node(0, 0, initial_genome, goal, None, divisor)

    # add first node to priority queue
    priority_queue.put((first_node.score, first_node))

    # create children and calculate misplaces
    first_node.createChildren(combinations, goal, divisor, priority_queue, archive)

    # check if it's not accidentally already sorted
    if first_node.misplacesSum == 0:
        solved = True
    else:
        solved = False

    # move first node to the archive
    archive.append(first_node)

    # repeat pathfinding until done
    while solved == False:
        # prune the priority queue
        if (len(priority_queue.queue) > 500000):
            highest = (priority_queue.queue[0][1]).steps
            for nodes in priority_queue.queue:
                if nodes[1].steps > highest:
                    highest = nodes[1].steps
            print "Step: ", highest
            priority_queue.queue = priority_queue.queue[0:200000]
        # print length
        print len(priority_queue.queue)
        
        # find node with lowest total in priority_queue
        priority_queue.queue[0][1].createChildren(combinations, goal, divisor, priority_queue, archive)
    
    # solution reached!
    print "Done!"
    for nodes in archive:
        if nodes.state == range(1, 26):
            print "Steps: ", nodes.steps, "\n"
            print "Genes transferred: ", nodes.genes, "\n", "\n"
            print "Solution: ", nodes.state, "\n"
            while nodes.parent != None:
                print "Previous: ", nodes.parent, "\n"

# define user interface
user_goal = input('Press 0 for minimum amount of inversions and 1 for minimum amount of inverted genes: ')
user_genome = input('Press 0 for D. melanogaster genome and 1 for random genome: ')
runProgram(user_goal, user_genome)
