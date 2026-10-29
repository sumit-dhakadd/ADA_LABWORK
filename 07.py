
import heapq

class ShortestPath:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.edges.append((u, v, w))

    def dijkstra(self, source):
        distance = [float('inf')] * self.n
        distance[source] = 0

        pq = [(0, source)]

        while pq:
            current_dist, node = heapq.heappop(pq)

            if current_dist != distance[node]:
                continue

            for neighbor, weight in self.graph[node]:
                new_dist = current_dist + weight

                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distance

    def bellman_ford(self, source):
        distance = [float('inf')] * self.n
        distance[source] = 0

        for i in range(self.n - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf'):
                    new_dist = distance[u] + weight

                    if new_dist < distance[v]:
                        distance[v] = new_dist

        for u, v, weight in self.edges:
            if distance[u] != float('inf'):
                if distance[u] + weight < distance[v]:
                    return "Error: Negative weight cycle detected"

        return distance


sp = ShortestPath(5)

sp.add_edge(0, 1, 4)
sp.add_edge(0, 2, 1)
sp.add_edge(2, 1, 2)
sp.add_edge(1, 3, 1)
sp.add_edge(2, 3, 5)
sp.add_edge(3, 4, 3)

print("Dijkstra:", sp.dijkstra(0))
print("Bellman-Ford:", sp.bellman_ford(0))
