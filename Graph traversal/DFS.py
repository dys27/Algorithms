from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.counter = 0
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.counter += 1
    
    def DFSUtil(self,v,visited):
        visited[v]= True
        print v
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self,v):
        visited = [False]* self.counter * self.counter
        self.DFSUtil(v,visited)
        
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is DFS from (starting from vertex 2)"
g.DFS(2)
