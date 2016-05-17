"""""""""""""""""""""""""""""""""""""""""""""""""""
 Gene Swapping - Basic Sort 100 random sample run
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 Team Melanogaster
 Jaap Nieuwenhuizen, Paul Berinde-Tampanariu, Merel van de Hurk
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random
subset_initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
subset_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]



steplist = []
genelist = []
for j in range (99):
    random.shuffle(subset_initial)
    #print subset_initial
    stepcounter = 0
    genecounter = 0
    for step in range(len(subset_initial)):
        if (subset_initial[step] != subset_solution[step]):
            swap=[]
            # find and select the index of the number to be swapped with n
            searchedI = subset_initial.index(subset_solution[step])
            # reversely iterate over the selected index to n
            for i in range(searchedI, (step - 1), -1):
                # append swapped row into swap list
                swap.append(subset_initial[i])
            genecounter = genecounter + (len(swap))
            # insert swap list into subset_initial
            for m in range(len(swap)):
                subset_initial[step + m] = swap[m]
            #genelist.append(genecounter)
            stepcounter += 1
    steplist.append(stepcounter)
    genelist.append(genecounter)
print "individual step results:", steplist    
print "individual gene results:", genelist
print "Average Steps=", (sum(steplist))/len(steplist)
print "Average Genes=", (sum(genelist))/len(genelist)