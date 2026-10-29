
import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    # Kruskal's Algorithm
    def kruskal_mst(self):
        parent = [i for i in range(self.n)]
        mst = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges = sorted(self.edges, key=lambda x: x[2])

        for u, v, w in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                mst.append((u, v, w))
                parent[root_u] = root_v

            if len(mst) == self.n - 1:
                break

        return mst

    # Prim's Algorithm
    def prim_mst(self):
        if self.n == 0:
            return []

        adj = [[] for _ in range(self.n)]

        for u, v, w in self.edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visited = [False] * self.n
        pq = [(0, 0, -1)]
        mst = []

        while pq:
            weight, node, parent = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True

            if parent != -1:
                mst.append((parent, node, weight))

            for neighbor, cost in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(
                        pq, (cost, neighbor, node)
                    )

        return mst


g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal MST:", g.kruskal_mst())
print("Prim MST:", g.prim_mst())
