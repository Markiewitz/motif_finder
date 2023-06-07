import itertools
import networkx as nx


def generate_permutations(n):
    # Define the number of nodes
    num_nodes = n
    graphs = []
    # Generate all possible edges
    edges = list(itertools.permutations(range(1, num_nodes + 1), 2))

    # Generate power set of edges
    power_set = itertools.chain.from_iterable(itertools.combinations(edges, r) for r in range(len(edges) + 1))

    # Iterate over each set of edges and create graphs
    for edge_set in power_set:
        # Create a directed graph
        G = nx.DiGraph()
        # Add nodes
        G.add_nodes_from(range(1, num_nodes + 1))
        # Add edges based on the set of edges
        G.add_edges_from(edge_set)

        # Check if the graph is connected and is not isomorphic with any existent
        if nx.number_weakly_connected_components(G) == 1 and not any((nx.vf2pp_is_isomorphic(G, G1) for G1 in graphs)):
            # Add the graph to the list
            graphs.append(G)
    final = []
    for graph in graphs:
        final.append(list(graph.edges))

    return final


def n_connected_subgraphs(output_file, s=1, e=1):
    # open output file
    file = open(output_file, "w")

    # loops over all sizes from s to e
    for n in range(s, e + 1):
        # generate motifs of size n
        permutations = generate_permutations(n)

        # write into output file
        file.write('n = %s' % (n))
        file.write('\ncount'.format(len(permutations)))
        i = 0
        for graph in permutations:
            if graph:
                i += 1
                file.write('\n#%s' % (i))
                for item in graph:
                    file.write("\n%s" % str(item))
        file.write('\n\n')

    file.close()


def generate_groups(tuples, k):
    # K int representing size of subgraphs to be returned
    # TUPLES is a list of touples representing the edges of a graph
    # Returns all subgraphs of size K in graph represented by TUPLES

    groups = []
    # get all nodes in the graph
    numbers = [num for tup in tuples for num in tup]
    unique_numbers = set(numbers)
    # create graph from the nodes and edges
    G = nx.DiGraph()
    # Add nodes
    G.add_nodes_from(unique_numbers)
    # Add edges based on the set of edges
    G.add_edges_from(tuples)
    # iterate over all possible combinations of k nodes in the graph
    for comb in itertools.combinations(unique_numbers, k):
        # get subgraph for each combination
        H = G.subgraph(comb)
        # if subgraph is a k connected subgraph add to groups
        if len(list(H.edges)) >= k - 1:
            groups.append(list(H.edges))
    return groups


def n_connected_subgraphs_count(in_graph, output_file, n=1):
    # open output file
    file = open(output_file, "w")
    # use generate_groups function to find all subgraphs in in_graph of size n
    subgraphs = generate_groups(in_graph, n)
    # use generate_permutations function to get all motifs of size n
    motifs = generate_permutations(n)
    # initialize count for all motifs
    count_motifs = [0] * len(motifs)
    # check for every subgraph of in_graph
    for graph in subgraphs:
        # get nodes
        numbers = [num for tup in graph for num in tup]
        unique_numbers = set(numbers)
        # convert list of edges to graph
        G = nx.DiGraph()
        # Add nodes
        G.add_nodes_from(unique_numbers)
        # Add edges based on the set of edges
        G.add_edges_from(graph)

        # check for every motif in motifs
        for index, sublist in enumerate(motifs):
            # convert list of tuples to graph
            G1 = nx.DiGraph()
            numbers1 = [num for tup in sublist for num in tup]
            unique_numbers1 = set(numbers1)
            G1.add_nodes_from(unique_numbers1)
            G1.add_edges_from(sublist)
            # if the subgraph G is isomorphic to any of the motifs then count
            if nx.vf2pp_is_isomorphic(G, G1):
                count_motifs[index] += 1
    i = 0
    # print to output file
    for motif in motifs:
        file.write('#%s' % (i + 1))
        file.write('\ncount = %s' % (count_motifs[i]))
        i += 1
        for item in motif:
            file.write("\n%s" % str(item))
        file.write('\n\n')

    file.close()
