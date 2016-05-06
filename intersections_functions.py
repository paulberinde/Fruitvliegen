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
