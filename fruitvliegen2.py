subset_initial = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9];
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];
# todo: build a randomizer for indices
subset_random = [];
counter = 0;

for step in range(len(subset_initial)):
    if (subset_initial[step] != subset_solution[step]):
        # find and select the index of the number to be swapped with n
        searchedI = subset_initial.index(subset_solution[step]);
        swap = [];

        # reversely iterate over the selected index to n
        for i in range(searchedI, (step - 1), -1):
            # append swapped row into swap list
            swap.append(subset_initial[i]);

        # insert swap list into subset_initial
        for m in range(len(swap)):
            subset_initial[step + m] = swap[m];
        counter += 1;

# print amount of steps
print "Steps:", counter;

#todo: detect patterns (such as 12:17), with, for example, a for-loop which takes and swaps with the highest index..
# and stores the length of the pattern to swap the current index with again (that is, swap step with step + len(pattern)).
#todo: order at the right end of the list and compare steps
