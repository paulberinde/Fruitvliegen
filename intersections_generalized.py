# declare Melanogaster and Miranda genomes for reference
genome_first = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
genome_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
misplaced = []

#
# This code creates an array of numbers which are based on the difference between
# the current index of the element and the place it should end up (in other words, how
# many places it's removed from its final place).
#

# calculate difference between current index and desired index
for gene in genome_first:
    misplaced.append(genome_end.index(gene) - genome_first.index(gene))

print misplaced




#
# This code creates an array of numbers which are based on the intersections between
# elements (in other words, how many elements have to "cross over" that element in
# reference to the final sorted array).
#

# initialize variables
intersections = []
# calculate intersections per element
for gene in genome_first:
    counter = 0
    for element in genome_first:
        if genome_first.index(element) < genome_first.index(gene):
            if genome_end.index(element) > genome_end.index(gene):
                counter += 1
        elif genome_first.index(element) > genome_first.index(gene):
            if genome_end.index(element) < genome_end.index(gene):
                counter += 1
    intersections.append(counter)

print intersections
