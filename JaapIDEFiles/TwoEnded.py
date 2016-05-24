"""""""""""""""""""""""""""
 Two-Ended Basic Sorting
"""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 Team Melanogaster
 Jaap Nieuwenhuizen, Paul Berinde-Tampanariu, Merel van de Hurk
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# import
import random

# define functions for colored prints
def prRed(prt): return("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): return("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): return("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): return("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): return("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): return("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): return("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): return("\033[98m {}\033[00m" .format(prt))

class TwoEndedSwap(object):
    """
    Represents a sorting algorithm.
    
    At all times the sorting class has a particular initial subset and solution subset.
    It also has a counter, switcher boolean, pattern length and searched index variables.
    
    Subclasses of TwoEndedSwap are a variant on pancake sorting / selection sort.
    It selects the lowest number, and moves this number to the front of the list.
    """

    def __init__(self, subset_initial, subset_solution):
        """
        Define initial variables. Turn initial and solution subset into global arrays.
        """
        
        # the initial and solution subset
        self.subset_initial = subset_initial
        self.subset_solution = subset_solution
        
        # implement error checking
        if (sorted(subset_initial) != sorted(subset_solution)):
            print "Error! The inserted subsets do not contain the same numbers."
            raise ValueError("Error! The inserted subsets do not contain the same numbers.")
        
        '''
        Keeps track of the number of the total steps,
        the low and the high end progression,
        the length of the subsets (which should always be equal),
        and the preferences and transferred gene count.
        '''
        self.counter = 0
        self.low = 0
        self.high = 0
        self.length = len(self.subset_initial)
        self.storePref = []
        self.transferredGenes = 0
    
    def introInitialisation(self):
        """
        Print an introduction and initialise the initial subset/genome and solution subset.
        The initial subset will have to be swapped around to get to the solution subset.
        """
        
        # print introduction
        print "Initial:{}".format(prPurple(self.subset_initial))
        print "Solution:{}\n".format(prCyan(self.subset_solution))
        print(prGreen("Let's sort..."))

    def initVariables(self):
        """
        Initialise and reset all necessary helper variables for swapping.
        These variables will be inserted into other functions.
        """
        
        # find and store the index of the number to be swapped and make a copy of it
        self.searchedILow = (self.subset_initial).index(self.subset_solution[self.low])
        self.iSearchLow = self.searchedILow
        self.searchedIHigh = (self.subset_initial).index(self.subset_solution[(self.length - 1) - self.high])
        self.iSearchHigh = self.searchedIHigh
        
        # set preference for lower end
        if ((self.iSearchLow - self.low) <= ((self.length - 1) - (self.iSearchHigh + self.high))):
            self.preference = True
        else:
            self.preference = False
        
        # store preference
        (self.storePref).append(self.preference)
        
        # reset swap, patlen and switcher
        self.swap = []
        self.patlen = 1
        self.switcher = False

    def calcMisplacement(self):
        self.misplaced = []
        
        '''
        This code creates an array of numbers which are based on the difference between
        the current index of the element and the place it should end up (in other words, how
        many places it's removed from its final place).
        '''
        
        # calculate difference between current index and desired index
        for gene in self.subset_initial:
            (self.misplaced).append((self.subset_solution).index(gene) - (self.subset_initial).index(gene))

    def calcIntersection(self):
        '''
        This code creates an array of numbers which are based on the intersections between
        elements (in other words, how many elements have to "cross over" that element in
        reference to the final sorted array).
        '''
        
        # initialize variables
        self.intersections = []
        # calculate intersections per element
        for gene in self.subset_initial:
            counter = 0
            for element in self.subset_initial:
                if ((self.subset_initial).index(element) < (self.subset_initial).index(gene)):
                    if ((self.subset_solution).index(element) > (self.subset_solution).index(gene)):
                        counter += 1
                elif ((self.subset_initial).index(element) > (self.subset_initial).index(gene)):
                    if ((self.subset_solution).index(element) < (self.subset_solution).index(gene)):
                        counter += 1
            (self.intersections).append(counter)

    def swapPattern(self):
        """
        Search for a pattern/group in the subset.
        If the subset is followed by incremental numbers, swap the highest number with the lowest.
        """
        
        if (self.preference == True):
            '''
            This is pattern recognition for the lower end.
            '''
            for recognition in range(self.length):
                if (self.searchedILow != self.length - 1):
                    if (self.subset_initial[self.searchedILow] + 1 == self.subset_initial[self.searchedILow + 1]):
                        self.searchedILow += 1
                        self.patlen += 1
                        self.switcher = True
            
            '''
            This is pattern swapping for the lower end.
            '''
            # reversely iterate over the pattern
            for pattern in range((self.iSearchLow + (self.patlen - 1)), (self.iSearchLow - 1), -1):
                # append swapped pattern row into swap list
                (self.swap).append(self.subset_initial[pattern])
            
            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                (self.subset_initial)[self.iSearchLow + insert] = self.swap[insert]
            
            # increase counter by one and print swap
            if (self.switcher == True):
                self.counter += 1
                print "Step", self.counter, ":", self.subset_initial
                print "Reversed:{}".format(prRed(self.swap))
                
                # add the number of swapped genes to the transferred gene counter
                self.transferredGenes += self.patlen
                print "Transferred genes:", self.transferredGenes
        
        else:
            '''
            This is pattern recognition for the higher end.
            '''
            for recognition in range(self.length, - 1, - 1):
                if (self.searchedIHigh != 0):
                    if (self.subset_initial[self.searchedIHigh] - 1 == self.subset_initial[self.searchedIHigh - 1]):
                        self.searchedIHigh -= 1
                        self.patlen += 1
                        self.switcher = True

            '''
            This is pattern swapping for the higher end.
            '''
            # reversely iterate over the pattern
            for pattern in range((self.iSearchHigh - (self.patlen - 1)), self.iSearchHigh + 1):
                # append swapped pattern row into swap list
                (self.swap).append(self.subset_initial[pattern])
            
            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                (self.subset_initial)[self.iSearchHigh - insert] = self.swap[insert]
            
            # increase counter by one and print swap
            if (self.switcher == True):
                self.counter += 1
                print "Step", self.counter, ":", self.subset_initial
                print "Reversed:{}".format(prRed(self.swap))
                
                # add the number of swapped genes to the transferred gene counter
                self.transferredGenes += self.patlen
                print "Transferred genes:", self.transferredGenes

    def regularSwapping(self):
        """
        This is regular swapping.
        """
        
        # clear swap array
        self.swap = []
        
        if (self.preference == True):
            '''
            Regular inversion swapping for the lower end.
            '''
            # reversely iterate over the selected index to n
            for index in range(self.searchedILow, (self.low - 1), -1):
                # append swapped row into swap list
                (self.swap).append(self.subset_initial[index])
            
            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                self.subset_initial[self.low + insert] = self.swap[insert]
            
            # increase counter by one, update lower end and print swap
            self.counter += 1
            if (self.switcher == True):
                self.low += self.patlen
            else:
                self.low += 1
            print "Step", self.counter, ":", self.subset_initial
            print "Reversed:{}".format(prRed(self.swap))
            
            # add the number of swapped genes to the transferred gene counter
            self.transferredGenes += len(self.swap)
            print "Transferred genes:", self.transferredGenes
        
        else:
            '''
            Regular inversion swapping for the higher end.
            '''
            # reversely iterate over the selected index to n
            for index in range(self.searchedIHigh, self.length - self.high):
                # append swapped row into swap list
                (self.swap).append(self.subset_initial[index])
            
            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                self.subset_initial[((self.length - 1) - self.high) - insert] = self.swap[insert]
            
            # increase counter by one, update higher end and print swap
            self.counter += 1
            if (self.switcher == True):
                self.high += self.patlen
            else:
                self.high += 1
            print "Step", self.counter, ":", self.subset_initial
            print "Reversed:{}".format(prRed(self.swap))
            
            # add the number of swapped genes to the transferred gene counter
            self.transferredGenes += len(self.swap)
            print "Transferred genes:", self.transferredGenes

    def runSimulation(self):
        """
        Run a simulation.
        """
        
        '''
        Print an introduction.
        '''
        self.introInitialisation()
        
        # iterate over the length of the subsets
        for step in range(self.length):
            '''
            Calculate intersections and misplaced tiles for determining the preference.
            '''
            '''
            self.calcMisplacement()
            self.calcIntersection()
            '''
            
            '''
            Initialize/reset variables.
            '''
            if (self.subset_initial != self.subset_solution):
                self.initVariables()
                
                # RUN THE ALGORITHM
                if (self.preference == True):
                    # check low end
                    if (self.subset_initial[self.low] != self.subset_solution[self.low]):
                        '''
                        Search for a pattern/group at the searched index (if one exists),
                        and inverse swap this group.
                        '''
                        self.swapPattern()
                        
                        '''
                        This is regular swapping.
                        '''
                        self.regularSwapping()
                    else:
                        # the low end number is already in the correct position
                        self.low += 1
                else:
                    # check high end
                    if (self.subset_initial[(self.length - 1) - self.high] != self.subset_solution[(self.length - 1) - self.high]):
                        '''
                        Search for a pattern/group at the searched index (if one exists),
                        and inverse swap this group.
                        '''
                        self.swapPattern()
                        
                        '''
                        This is regular swapping.
                        '''
                        self.regularSwapping()
                    else:
                        # the high end number is already in the correct position
                        self.high += 1
        
        # print amount of steps
        print ("{}\n").format(prGreen("That's all!"))
        print "Total steps:{}".format(prYellow(self.counter))
        print "Total transferred genes:{}".format(prYellow(self.transferredGenes))
        print "Preferences:{}".format(prYellow(self.storePref))
        return True

'''
Test the class.
'''
subset_initial = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# random.shuffle(subset_initial)
subsetsObject = TwoEndedSwap(subset_initial, subset_solution)
subsetsObject.runSimulation()
