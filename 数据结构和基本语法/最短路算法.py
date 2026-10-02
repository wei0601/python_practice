class Graph:
    def __init__(self):
        self.graph = {}
class Dijkstra:
    def dijkstra(self,graph,start):
        dist = {node: float('inf') for node in graph}
        #记录目前已知的最短距离 全部初始化为无穷大
        visited = set()
        dist[start] = 0
        while len(visited)< len(graph):
            current = None
            #以下循环目的是找到距离最短的未访问的节点#
            for node in graph:
                if node not in visited:
                    if current == None:
                        current = node
                    elif dist[node] < dist[current]:
                        current = node 
            visited.add(current)
            for neighbor, weight in graph[current].items():
                new_dist =  dist[current] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
        return dist
def main():
    graph = Graph()
    # Add edges to the graph
    graph.graph['A'] = {'B': 4, 'C': 2}
    graph.graph['B'] = { 'C': 1, 'D': 5}
    graph.graph['C'] = { 'D': 8,'E': 10}
    graph.graph['D'] = {'E': 2}
    graph.graph['E'] = {}

    dijkstra = Dijkstra()
    distances = dijkstra.dijkstra(graph.graph, 'A')
    print("Shortest distances from node A:", distances)

if __name__ == "__main__":
    main()  