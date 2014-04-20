# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


# assume for each edge, edge[0] < edge[1]
def find_eulerian_tour(graph):
    # determine if a eulerian tour exists
    degree_dict = {}
    
    for edge in graph:
        for node in edge:
            if degree_dict.get(node) == None:
                degree_dict[node] = 1
            else:
                degree_dict[node] = degree_dict[node] + 1
    
    overall_degree = 0
    tour = []
    for key in degree_dict:
        if degree_dict[key] % 2 == 1:
            print "cannot find Eulerian Tour"
            return False
        
        else:
            # use dictionary to build a map
            for edge in graph:
                for node in edge:
                    tour.append(node)
                    
            
            return tour
                
                    
            


print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])