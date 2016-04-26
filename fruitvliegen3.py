# initialize subsets
subset_initial = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9];
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];

# store number of conflicts
# update number of conflicts
# etc.
# simulated annealing?? (probability of switching something that doesn't resolve conflicts)

# todo: build a randomizer for indices
subset_random = [];
counter = 0;

# print introduction
print "Initial: ", subset_initial;
print "Solution: ", subset_solution, "\n";
print "Let's sort...";

# the algorithm for basic swapping
for step in range(len(subset_initial)):
    if (subset_initial[step] != subset_solution[step]):
        '''
        Initialize variables
        '''
        # find and select the index of the number to be swapped with n
        searchedI = subset_initial.index(subset_solution[step]);
        swap = [];
        patlen = 0;
        switcher = False;

        '''
        Search for a pattern/group
        '''
        # find pattern if it exists
        for pattern in range(len(subset_initial)):
            if (searchedI != len(subset_initial) - 1):
                if (subset_initial[searchedI] + 1 == subset_initial[searchedI + 1]):
                    searchedI += 1;
                    patlen += 1;
                    switcher = True;

        '''
        This is regular swapping
        '''
        # reversely iterate over the selected index to n
        for i in range(searchedI, (step - 1), -1):
            # append swapped row into swap list
            swap.append(subset_initial[i]);

        # insert swap list into subset_initial
        for m in range(len(swap)):
            subset_initial[step + m] = swap[m];
        counter += 1;
        print subset_initial;

        '''
        This is pattern swapping
        '''
        # swap the reversed pattern back
        if switcher == True:
            swap = [];
            # reversely iterate over the pattern
            for pattern in range((step + patlen), (step - 1), -1):
                # append swapped pattern row into swap list
                swap.append(subset_initial[pattern]);

            # insert swap list into subset_initial
            for m in range(len(swap)):
                subset_initial[step + m] = swap[m];
            counter += 1;
            print subset_initial;

# print amount of steps
print "Steps:", counter;


'''
# find pattern if it exists
for pattern in range(len(subset_initial)):
    if (subset_initial[searchedI] + 1 == subset_initial[searchedI + 1]):
        searchedI += 1;
        patlen += 1;
        switcher = True;

# swap the reversed pattern back
if switcher == True:
    swap = [];
    # reversely iterate over the pattern
    for pattern in range((step + patlen), (step - 1), -1):
        # append swapped pattern row into swap list
        swap.append(subset_initial[pattern]);

    # insert swap list into subset_initial
    for m in range(len(swap)):
        subset_initial[step + pattern] = swap[pattern];
    counter += 1;
'''
