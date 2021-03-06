"""""""""""""""""""""""""""
 Two-Ended Basic Swapping
"""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 Team Melanogaster
 Jaap Nieuwenhuizen, Paul Berinde-Tampanariu, Merel van de Hurk
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class TwoEndedSwap(object):
    """
    Represents a swapping algorithm.
    
    At all times the robot has a particular initial subset and solution subset.
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
        and the length of the subsets (which should always be equal).
        '''
        self.counter = 0
        self.low = 0
        self.high = 0
        self.length = len(self.subset_initial) - 1

    def introInitialisation(self):
        """
        Print an introduction and initialise the initial subset/genome and solution subset.
        The initial subset will have to be swapped around to get to the solution subset.
        """

        # print introduction
        print "Initial: ", self.subset_initial
        print "Solution: ", self.subset_solution, "\n"
        print "Let's sort..."

    def initVariables(self):
        """
        Initialise and reset all necessary helper variables for swapping.
        These variables will be inserted into other functions.
        """

        # find and store the index of the number to be swapped and make a copy of it
        self.searchedILow = (self.subset_initial).index(self.subset_solution[self.low])
        self.iSearchLow = self.searchedILow
        self.searchedIHigh = (self.subset_initial).index(self.subset_solution[self.length - self.high])
        self.iSearchHigh = self.searchedIHigh

        # set preference for lower end
        if ((self.iSearchLow - self.low) <= (self.length - (self.iSearchHigh + self.high))):
            self.preference = True
        else:
            self.preference = False

        # reset swap, patlen and switcher
        self.swap = []
        self.patlen = 0
        self.switcher = False

    def swapPattern(self):
        """
        Search for a pattern/group in the subset.
        If the subset is followed by incremental numbers, swap the highest number with the lowest.
        """

        if (self.preference == True):
            '''
            This is pattern recognition for the lower end.
            '''
            for recognition in range(self.length + 1):
                if (self.searchedILow != self.length):
                    if (self.subset_initial[self.searchedILow] + 1 == self.subset_initial[self.searchedILow + 1]):
                        self.searchedILow += 1
                        self.patlen += 1
                        self.switcher = True

            '''
            This is pattern swapping for the lower end.
            '''
            # reversely iterate over the pattern
            for pattern in range((self.iSearchLow + self.patlen), (self.iSearchLow - 1), -1):
                # append swapped pattern row into swap list
                (self.swap).append(self.subset_initial[pattern])

            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                (self.subset_initial)[self.iSearchLow + insert] = self.swap[insert]

            # increase counter by one and print swap
            if (self.switcher == True):
                self.counter += 1
                print "Step", self.counter, ":", self.subset_initial

        else:
            '''
            This is pattern recognition for the higher end.
            '''
            for recognition in range(self.length + 1):
                if (self.searchedIHigh != 0):
                    if (self.subset_initial[self.searchedIHigh] - 1 == self.subset_initial[self.searchedILow - 1]):
                        self.searchedIHigh -= 1
                        self.patlen += 1
                        self.switcher = True

            '''
            This is pattern swapping for the higher end.
            '''
            # reversely iterate over the pattern
            for pattern in range((self.iSearchHigh - self.patlen), self.iSearchHigh + 1):
                # append swapped pattern row into swap list
                (self.swap).append(self.subset_initial[pattern])

            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                print self.iSearchHigh - insert, self.length + insert
                (self.subset_initial)[self.iSearchHigh - insert] = self.swap[insert]

            # increase counter by one and print swap
            if (self.switcher == True):
                self.counter += 1
                print "Step", self.counter, ":", self.subset_initial

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

        else:
            '''
            Regular inversion swapping for the higher end.
            '''
            # reversely iterate over the selected index to n
            for index in range(self.searchedIHigh, self.length + 1 - self.high):
                # append swapped row into swap list
                (self.swap).append(self.subset_initial[index])

            # insert swap list into subset_initial
            for insert in range(len(self.swap)):
                self.subset_initial[(self.length - self.high) - insert] = self.swap[insert]

            # increase counter by one, update higher end and print swap
            self.counter += 1
            if (self.switcher == True):
                self.high += self.patlen
            else:
                self.high += 1
            print "Step", self.counter, ":", self.subset_initial

    def runSimulation(self):
        """
        Run a simulation.
        """

        '''
        Print an introduction.
        '''
        self.introInitialisation()

        # iterate over the length of the subsets
        for step in range(self.length + 1):
            '''
            Initialize/reset variables.
            '''
            self.initVariables()

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
                if (self.subset_initial[self.length - self.high] != self.subset_solution[self.length - self.high]):
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
        print "Steps:", self.counter
        return True

'''
Test the class.
'''
subset_initial = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
subsetsObject = TwoEndedSwap(subset_initial, subset_solution)
subsetsObject.runSimulation()
