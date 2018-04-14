from collections import defaultdict
graph = defaultdict(list)
V = 4
 
def addEdge(u,v):
    graph[u].append(v)
 
def isCyclicUtil(v, visited, recStack):
    visited[v] = True
    recStack[v] = True
    for i in graph[v]:
        if visited[i] == False:
            if isCyclicUtil(i, visited, recStack) == True:
                return True
        elif recStack[i] == True:
            return True
    recStack[v] = False
    return False
 
# Returns true if graph is cyclic else false
def isCyclic():
    visited = [False] * V
    recStack = [False] * V
    for j in range(V):
        if visited[j] == False:
            if isCyclicUtil(j,visited,recStack) == True:
                return True
    return False
    
