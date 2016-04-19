
subset_1 = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9];
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];

for step in range(len(subset_1)):
    if (subset_1[step] != subset_solution[step]):
        # find and select the index of the number to be swapped with n
        searchedI = subset_1.index(subset_solution[step]);
        print searchedI;
        # reversely iterate over the selected index to n
        for i in range(searchedI, step, -1):
            # create a temporary swap list
            swap = [];
            swap.append(subset_1[searchedI]);
            
            # insert swap list into subset_1
            for m in range(len(swap)):
                subset_1[step + m] = swap[m];
            print step;
            print subset_1;
            
        #for (i = temporary; i > n; i--):
        


            