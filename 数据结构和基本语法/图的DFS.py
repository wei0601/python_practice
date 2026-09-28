class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
class DFS:
    def dfs(self,graph,start):
        visitied = set()
        result = []
        self.dfs_util(graph,start,visitied,result)
        return result
    def dfs_util(self,graph,start,visitied,result):
        visitied.add(start)
        result.append(start)
        for x in graph.graph[start]:
            if x not in visitied:
                self.dfs_util(graph,x,visitied,result)
def main():
    graph = Graph(5)
    graph.graph[0].append(1)
    graph.graph[0].append(2)
    graph.graph[1].append(3)
    graph.graph[2].append(3)
    graph.graph[3].append(4)
    dfs = DFS()
    print(dfs.dfs(graph,0))
if __name__ == "__main__":
    main()



