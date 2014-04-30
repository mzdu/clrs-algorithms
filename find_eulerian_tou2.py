from collections import defaultdict
from random import choice
def find_eulerian_tour(graph):
    # nodes: dictionary of edges to travel in the form {node: list of nodes connected to that node}
    nodes = defaultdict(list)
    for k,l in graph:
        nodes[k].append(l)
        nodes[l].append(k)

    # pick a random node to begin the path
    node = choice(nodes.keys())
    path = [node]

    # traverse the graph. remove used edges as you go
    while len(nodes[node]) > 0 :
        after = nodes[node].pop()
        nodes[after].remove(node)      
        path.append(after)
        node = after

    # find nodes in our path that still have unused edges
    for node, node_list in nodes.iteritems():
        if node in path and len(node_list)>0:

            # insert "detour" into our path. as before, remove edges as you go
            index = path.index(node)
            while len(nodes[node]) > 0 :
                after = nodes[node].pop()
                nodes[after].remove(node)
                index+=1
                path.insert(index,after)
                node = after

    return path


case1 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

case2 = [(1, 2), (2, 3), (3, 1)]

case3 = [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]

case4 = [(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]


print find_eulerian_tour(case4)