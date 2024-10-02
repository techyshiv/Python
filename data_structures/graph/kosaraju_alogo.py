from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with a given number of vertices.
        
        Args:
            vertices (int): The number of vertices in the graph.
        """
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Default dictionary to store the graph
    
    def add_edge(self, u, v):
        """
        Add a directed edge from vertex u to vertex v.
        
        Args:
            u (int): The starting vertex of the edge.
            v (int): The ending vertex of the edge.
        """
        self.graph[u].append(v)
    
    def _dfs(self, v, visited, stack=None):
        """
        A recursive function to perform DFS from vertex v.
        If stack is provided, it pushes the vertices in the order of their finish time.
        
        Args:
            v (int): The starting vertex for the DFS.
            visited (list[bool]): A list to keep track of visited vertices.
            stack (list[int]): A stack to store the finish time order of vertices.
        """
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(v)
    
    def _transpose(self):
        """
        Function to transpose (reverse) the graph.
        
        Returns:
            Graph: The transposed graph.
        """
        transposed = Graph(self.V)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed.add_edge(neighbor, vertex)
        return transposed
    
    def kosaraju_scc(self):
        """
        Find all Strongly Connected Components (SCCs) in the graph using Kosaraju's Algorithm.
        
        Returns:
            list[list[int]]: A list of SCCs, where each SCC is a list of vertices.
        
        Examples:
            >>> g = Graph(5)
            >>> g.add_edge(1, 0)
            >>> g.add_edge(0, 2)
            >>> g.add_edge(2, 1)
            >>> g.add_edge(0, 3)
            >>> g.add_edge(3, 4)
            >>> g.kosaraju_scc()
            [[0, 1, 2], [3], [4]]
            
            >>> g2 = Graph(4)
            >>> g2.add_edge(0, 1)
            >>> g2.add_edge(1, 2)
            >>> g2.add_edge(2, 0)
            >>> g2.add_edge(2, 3)
            >>> g2.kosaraju_scc()
            [[0, 1, 2], [3]]
            
            >>> g3 = Graph(8)
            >>> g3.add_edge(0, 1)
            >>> g3.add_edge(1, 2)
            >>> g3.add_edge(2, 3)
            >>> g3.add_edge(2, 4)
            >>> g3.add_edge(3, 0)
            >>> g3.add_edge(4, 5)
            >>> g3.add_edge(5, 6)
            >>> g3.add_edge(6, 4)
            >>> g3.add_edge(6, 7)
            >>> g3.kosaraju_scc()
            [[0, 1, 2, 3], [4, 5, 6], [7]]
        """
        stack = []
        visited = [False] * self.V
        
        # First pass: Fill the stack with vertices in finishing time order
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        
        # Step 2: Get the transposed graph
        transposed_graph = self._transpose()
        
        # Step 3: Process vertices in order of their finish times
        visited = [False] * self.V
        sccs = []
        
        while stack:
            v = stack.pop()
            if not visited[v]:
                scc_stack = []
                transposed_graph._dfs(v, visited, scc_stack)
                # Sort the SCC for consistent order in output
                sccs.append(sorted(scc_stack))
        
        # Sort the list of SCCs for consistent ordering
        return sorted(sccs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
