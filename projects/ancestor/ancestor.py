 #make graph to store the relations
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
    #check for longest path to return but keep track of the other paths
    graph = Graph()
    for pair in ancestors:
        graph.add_vert(pair[1])
    for pair2 in ancestors:
        graph.add_vert(pair2[0])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    
    print(graph.verts)
    if len(graph.verts[starting_node]) == 0:
        return -1
    
    stack = []
    stack.append([starting_node])
    current_path = stack
    while len(stack) > 0:
        old_path = current_path
        current_path = stack.pop()
        current = current_path[-1]
        
        for next_node in graph.get_neighbor(current):
            new_path = list(current_path)
            new_path.append(next_node)
            stack.append(new_path)
            
    if len(current_path) > len(old_path):
        return current_path[-1]
    elif len(current_path) == len(old_path):
        if old_path[-1] < current_path[-1]:
            return old_path[-1]
if __name__ == '__main__':
    test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test, 9))