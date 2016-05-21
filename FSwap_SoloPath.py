"""""""""""""""""""""""""""
 Gene Swapping Algorithm
"""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 Team Melanogaster
 Jaap Nieuwenhuizen, Paul Berinde-Tampanariu, Merel van de Hurk
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# import
import random
import itertools

# define functions for colored prints
def prRed(prt): return("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): return("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): return("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): return("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): return("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): return("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): return("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): return("\033[98m {}\033[00m" .format(prt))

class FinalSwap(object):
    def __init__(self, genome_first, genome_end):
        """
        Define initial variables. Turn initial and solution subset into global lists.
        """
        self.genome_first = genome_first
        self.genome_end = genome_end
        self.steps = 0
        self.genes = 0
        self.positions = range(0, 25)
        
        # implement error checking
        if (sorted(self.genome_first) != sorted(self.genome_end)):
            print "Error! The inserted subsets do not contain the same numbers."
            raise ValueError("Error! The inserted subsets do not contain the same numbers.")
        
        """
        Print an introduction and initialise the initial set/genome and solution set.
        The initial set will have to be swapped around to get to the solution set.
        """
        print "Initial:{}".format(prPurple(self.genome_first))
        print "Solution:{}\n".format(prCyan(self.genome_end))
        print(prGreen("Let's sort..."))

    def combinator(self):
        """
        Compute all possible combinations of two genes.
        """
        comb_len = 2
        self.combinations = []
        for subset in itertools.combinations(self.positions, comb_len):
            (self.combinations).append(subset)

    def computeChildren(self):
        """
        Compute all possible children of genome_first.
        """
        self.children = []
        for child in range(len(self.combinations)):
            parent = list(self.genome_first)
            start = (self.combinations)[child][0]
            end = (self.combinations)[child][1] + 1
            parent[start:end] = (self.genome_first)[start:end][::-1]
            (self.children).append(parent)

    def getMisplaces(self, genome_insert):
        """
        Compute a list of index misplacement-values with genome_insert.
        """
        #print "Insert: ", genome_insert
        self.misplaces = []
        for gene in genome_insert:
            (self.misplaces).append((self.genome_end).index(gene) - (genome_insert).index(gene))

    def runSimulation(self, times):
        """
        Run a simulation x times.
        """
        self.combinator()
        for step in range(times):
            # run the combinator and compute all children
            self.computeChildren()
            
            # create a list for the sum of misplacements
            self.misplacesChild = []
            
            # compute misplacements-values of every child and add the sum to a list
            for child in self.children:
                self.getMisplaces(child)
                (self.misplacesChild).append(sum(map(abs, self.misplaces)))
            
            # select the child with the lowest sum of misplaces
            chosenOne = self.children[(self.misplacesChild).index(min(self.misplacesChild))]
            print "Step", (step + 1), ": ", chosenOne
            
            # update genes
            for gene in self.positions:
                if (self.genome_first[gene] != chosenOne[gene]):
                    self.genes += 1
            
            # update steps
            self.steps = step + 1
            
            # promote this child to self.genome_first
            self.genome_first = chosenOne
            
            # compare it with the genome_end
            if (self.genome_first == self.genome_end):
                "Done!"
                break
        print self.genome_first

# Test the class
genome_first = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
genome_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
objectFinalSwap = FinalSwap(genome_first, genome_end)
objectFinalSwap.runSimulation(20)
