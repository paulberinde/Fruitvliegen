# declare Melanogaster and Miranda genomes for reference
genome_first = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9];
genome_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];
intersections = [];

#
# This code creates an array of numbers which are based on the difference between
# the current index of the element and the place it should end up (in other words, how
# many places it's removed from its final place).
#

# calculate difference between current index and desired index
for gene in genome_first:
    intersections.append((gene - 1) - genome_first.index(gene));

print intersections;




#
# This code creates an array of numbers which are based on the intersections between
# elements (in other words, how many elements have to "cross over" that element in
# reference to the final sorted array).
#

# initialize variables
crossovers = [];
# calculate intersections per element
for gene in genome_first:
    counter = 0;
    for element in genome_first:
        if genome_first.index(element) < genome_first.index(gene):
            if element > gene:
                counter += 1;
        elif genome_first.index(element) > genome_first.index(gene):
            if element < gene:
                counter += 1;
    crossovers.append(counter);

print crossovers;
