from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=' ')

        for neighbor in sorted(self.graph[node]):
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if not visited[node]:
                print(node, end=' ')
                visited[node] = True
                neighbors = sorted(self.graph[node])
                queue.extend(neighbors)

    def has_cycle(self):
        visited = [False] * (max(self.graph) + 1)
        parent = [-1] * (max(self.graph) + 1)

        for node in sorted(self.graph):
            if not visited[node]:
                if self.detect_cycle_dfs(node, visited, parent):
                    return True

        return False

    def detect_cycle_dfs(self, node, visited, parent):
        visited[node] = True

        for neighbor in sorted(self.graph[node]):
            if not visited[neighbor]:
                parent[neighbor] = node
                if self.detect_cycle_dfs(neighbor, visited, parent):
                    return True
            elif parent[node] != neighbor:
                return True

        return False

    def is_bipartite(self):
        color = [-1] * (max(self.graph) + 1)

        for node in sorted(self.graph):
            if color[node] == -1:
                if not self.bipartite_bfs(node, color):
                    return False

        return True

    def bipartite_bfs(self, start, color):
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in sorted(self.graph[node]):
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

        return True

    def find_cycles(self):
        visited = set()
        for node in sorted(self.graph):
            if node not in visited:
                self.detect_and_print_cycle(node, set(), set())

    def detect_and_print_cycle(self, node, visited, current_path):
        stack = [(node, None, set())]

        while stack:
            current, parent, current_path = stack.pop()

            if current not in visited:
                visited.add(current)
                current_path.add(current)

                for neighbor in sorted(self.graph[current]):
                    if neighbor not in visited:
                        stack.append((neighbor, current, set(current_path)))
                    elif neighbor != parent and neighbor in current_path:
                        # Found a cycle
                        cycle_list = list(current_path)
                        cycle_list.append(neighbor)
                        print("Cycle:", ' '.join(map(str, cycle_list)))
                        break

        visited.remove(node)

# Example usage
g = Graph()
edges =[(1, 3), (1, 4), (2, 1), (2, 3), (3, 4), (4, 1), (4, 2)]

for edge in edges:
    g.add_edge(edge[0], edge[1])

print("DFS:")
g.dfs(1, [False] * (max(max(edges, key=lambda x: max(x))) + 1))

print("\nBFS:")
g.bfs(1)

print("\nCycles:")
g.find_cycles() 

print("\nBipartiteness:")
if g.is_bipartite():
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")
