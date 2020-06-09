class Graph:
    def __init__(self):
        self.verts = {}
    
    def add_vert(self, vert_id):
        self.verts[vert_id] = set()
    
    def add_edge(self, v1, v2):
        # if v1 in self.verts and v2 in self.verts:
        self.verts[v1].add(v2)
    
    def get_neighbor(self, vert_id):
        return self.verts[vert_id]
    
def earliest_ancestor(ancestors, starting_node):
    pass
    
    
#make graph to store the relations
#add nodes to the graph = for each input make a 'node'
#connect the nodes with edges to make the relation complete
#use bfs to find the earliest ancestor
    #instead of returning the path like yesterday just return the node(index, value,etc)

if __name__ == '__main__':
            #skip                   #skip   #skip   #4{5}    #4{5,8} #skip
    test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    graph = Graph()
    for pair in test:
        graph.add_vert(pair[0])
        graph.add_vert(pair[1])
        graph.add_edge(pair[0], pair[1])
    print(graph.verts)