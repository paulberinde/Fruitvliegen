"""""""""""""""
 Basic Swapping
"""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 Team Melanogaster
 Jaap Nieuwenhuizen, Paul Berinde-Tampanariu, Merel van de Hurk
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class BasicSwap(object):
    """
    Represents a swapping algorithm.
    
    At all times the robot has a particular initial subset and solution subset.
    It also has a counter, switcher boolean, pattern length and searched index variables.
    
    Subclasses of BasicSwap are a variant on pancake sorting / selection sort.
    It selects the lowest number, and moves this number to the front of the list.
    """
    
    def __init__(self, subset_initial, subset_solution):
        """
        Define initial variables. Turn initial and solution subset into global arrays.
        """

        # the initial and solution subset
        self.subset_initial = subset_initial
        self.subset_solution = subset_solution

        # keeps track of the number of steps
        self.counter = 0

    def introInitialisation(self):
        """
        Print an introduction and initialise the initial subset/genome and solution subset.
        The initial subset will have to be swapped around to get to the solution subset.
        """

        # print introduction
        print "Initial: ", self.subset_initial
        print "Solution: ", self.subset_solution, "\n"
        print "Let's sort..."

    def initVariables(self, step):
        """
        Initialise and globalise all necessary helper variables for basic swapping.
        These variables will be inserted into other functions.
        """

        # find and store the index of the number to be swapped with step into searchedI
        self.searchedI = (self.subset_initial).index(self.subset_solution[step])
        self.iSearch = self.searchedI
        self.swap = []
        self.patlen = 0
        self.switcher = False

    def swapPattern(self):
        """
        Search for a pattern/group in the subset.
        If the subset is followed by incremental numbers, swap the highest number with the lowest.
        """
        
        '''
        This is pattern recognition.
        '''
        for recognition in range(len(self.subset_initial)):
            if (self.searchedI != len(self.subset_initial) - 1):
                if (self.subset_initial[self.searchedI] + 1 == self.subset_initial[self.searchedI + 1]):
                    self.searchedI += 1
                    self.patlen += 1
                    self.switcher = True

        '''
        This is pattern swapping.
        '''
        # reversely iterate over the pattern
        for pattern in range((self.iSearch + self.patlen), (self.iSearch - 1), -1):
            # append swapped pattern row into swap list
            (self.swap).append(self.subset_initial[pattern])

        # insert swap list into subset_initial
        for insert in range(len(self.swap)):
            (self.subset_initial)[self.iSearch + insert] = self.swap[insert]

        # increase counter by one and print swap
        if (self.switcher == True):
            self.counter += 1
            print self.subset_initial

    def regularSwapping(self, step):
        """
        This is regular swapping.
        """

        # clear swap array
        self.swap = []

        # reversely iterate over the selected index to n
        for iterator in range(self.searchedI, (step - 1), -1):
            # append swapped row into swap list
            (self.swap).append(self.subset_initial[iterator])

        # insert swap list into subset_initial
        for insert in range(len(self.swap)):
            self.subset_initial[step + insert] = self.swap[insert]

        # increase counter by one and print swap
        self.counter += 1
        print self.subset_initial

    def basicSwap(self):
        """
        Run a simulation.
        """
        
        '''
        Print an introduction and initialise variables.
        '''
        self.introInitialisation()
        
        for step in range(len(self.subset_initial)):
            if (self.subset_initial[step] != self.subset_solution[step]):
                '''
                Initialize/reset variables.
                '''
                self.initVariables(step)

                '''
                Search for a pattern/group at the searched index (if one exists),
                and inverse swap this group.
                '''
                self.swapPattern()

                '''
                This is regular swapping.
                '''
                self.regularSwapping(step)

        # print amount of steps
        print "Steps:", self.counter

'''
Test the class.
'''
subset_initial = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
subsetsObject = BasicSwap(subset_initial, subset_solution)
subsetsObject.basicSwap()
