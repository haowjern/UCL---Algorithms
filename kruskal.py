# kruskal's algorithm

def main():
    a1 = 'a1'
    a2 = 'a2'
    a3 = 'a3'
    a4 = 'a4'
    a5 = 'a5'
    a6 = 'a6'
    a7 = 'a7'

    nodes = [a1, a2, a3, a4, a5, a6, a7]
    new = {(a1,a2): 1, (a1,a4): 4, (a2,a3): 2, (a2,a4):6, (a2,a5):4, (a3,a5):5, (a3,a6):6, (a4,a7): 4, (a4,a5): 3,
           (a5,a6): 8, (a5,a7): 7, (a6, a7): 3}

    min_span_tree = kruskal(nodes, new)
    print(min_span_tree)



def kruskal(nodes, edges): # edges have weights
    """
    :param nodes: list of nodes
    :param edges: dictionary of edges as keys (tuples) and weights as values
    :return: minimum spanning tree, list of edges
    """

    sorted_edge_list = sorted(edges, key=edges.__getitem__)

    components = [[i] for i in nodes]
    min_tree = [] # doesn't tell you the cost, just tells you the minimum spanning tree

    for i in sorted_edge_list:
        u,v = i # u,v nodes for edge i
        ucomp_index = find_comp(u, components)
        vcomp_index = find_comp(v, components)

        if ucomp_index != vcomp_index:
            merge_comp(components, ucomp_index, vcomp_index)
            min_tree.append(i)

    return min_tree

def find_comp(x, comp):
    for i in range(0, len(comp)):
        if x in comp[i]:
            return i
    return False

def merge_comp(tree, comp1, comp2):
    tree[comp1] = tree[comp1]+tree[comp2] # join lists together
    tree.remove(tree[comp2])


if __name__ == '__main__': main()