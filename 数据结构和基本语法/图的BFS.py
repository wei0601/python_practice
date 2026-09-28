class Graph:
    def __init__(self):
        self.graph = {}

class BFS:
    def bfs(self, graph, start):
        visited = set()
        visited.add(start)
        queue = [start]
        while queue:
            node = queue.pop(0)
            print(node,end = '')
            for x in graph[node]:
                if x not in visited: 
                    visited.add(x) 
                    queue.append(x)
def main():
    graph = Graph() 
    graph.graph = { 
        'A' : ['B','C'], 
        'B' : ['A','D', 'E'], 
        'C' : ['A','F'], 
        'D' : ['B'], 
        'E' : ['B','F'], 
        'F' : ['C', 'E'] 
     } 
    bfs = BFS() 
    bfs.bfs(graph.graph, 'A') 
if __name__ == "__main__":
    main()  # 运行主函数
