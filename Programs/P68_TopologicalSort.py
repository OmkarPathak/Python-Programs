# Author: OMKAR PATHAK

# Time Complexity: O(|V| + |E|)
# One important point to remember is that topological sort can be applied only to acyclic graph.

class Graph():
    def __init__(self, count):
        self.vertex = {}
        self.count = count          # vertex count

    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]
            self.vertex[toVertex] = []

    def topologicalSort(self):
        visited = [False] * self.count           # Marking all vertices as not visited
        stack = []                               # Stack for storing the vertex
        for vertex in range(self.count):
            # Call the recursive function only if not visited
            if visited[vertex] == False:
                self.topologicalSortRec(vertex, visited, stack)

        print(' '.join([str(i) for i in stack]))
        # print(stack)

    # Recursive function for topological Sort
    def topologicalSortRec(self, vertex, visited, stack):

        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        try:
            for adjacentNode in self.vertex[vertex]:
                if visited[adjacentNode] == False:
                    self.topologicalSortRec(adjacentNode, visited, stack)
        except KeyError:
            return

        # Push current vertex to stack which stores the result
        stack.insert(0,vertex)

if __name__ == '__main__':
    g= Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    # g.printGraph()
    g.topologicalSort()

    # OUTPUT:
    # 5 4 2 3 1 0
