# motif_finder
Network motif finder in graph represented network

With this code you will be able to:

 a. Compute all motifs, connected subgraphs, for n nodes.
 
 b. Given a graph with m nodes, find all n-node motifs present in the graph and it's frequencies.
 
## Compute All Motifs of Size n

*generate_permutations* function get as input the number of nodes n for the connected subgraphs and returns a list with all the connected subgraphs.

Each list is a list of tuples, where every touple represents a directed edge in the graph. For example (1,2) is the edges that has origin in 1 and ends in 2.

To compute motifs for more than one n, use function *n_connected_subgraphs* which receives as input a string representing the output file; int s with default 1, smallest size of graph desired; and int e for the biggest size of graph desired. The function will write its results to the output file, for every size n it will return the amount of connected graphs found and print them. 

## Find and Count all Motifs of size n in a Graph

*n_connected_subgraphs_count* will receive as an input a list of touples representing the edges of the graph; a string representing the output file; n to be the size of the motifs to find. For example, for n = 3, the function will find all subgraphs of size 3, recognize the motif and count it.

Output will be a file with all motifs of size n, for each motif the function will write the counts, if the motif is not present in the graph it will nevertheless be in the file but with count = 0. 
