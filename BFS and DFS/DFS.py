from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start_vertex):
        visited = [False] * len(self.graph)
        stack = [start_vertex]

        while stack:
            current_vertex = stack.pop()

            if not visited[current_vertex]:
                visited[current_vertex] = True
                print(current_vertex, end=" ")

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)
