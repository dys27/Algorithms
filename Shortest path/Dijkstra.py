import sys
import heapq
class vertex(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor = None
        self.adjacenciesList=[]
        self.minDistance=sys.maxsize

    def __cmp__(self,otherVertex):
        return self.cmp(self.minDistance,otherVertex.minDistance)

    def __lt__(self,other):
        selfPriority=self.minDistance
        otherPriority=other.minDistance
        return selfPriority<otherPriority

class edge(object):
    def __init__(self,weight,startVertex,targetVertex):
        self.weight = weight
        self.startVertex=startVertex
        self.targetVertex=targetVertex

class Algorithm(object):

    def calculateShortestPath(self,vertexList,startVertex):
        queue=[]
        startVertex.minDistance=0
        heapq.heappush(queue,startVertex)

        while len(queue)>0:
            actualVertex=heapq.heappop(queue)
   
            for edge in actualVertex.adjacenciesList:
                u=edge.startVertex
                v=edge.targetVertex
                newDistance=u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue,v)
    def getShortestPathTo(self,targetVertex):
        print "Shortest path to target is: ",targetVertex.minDistance

        node=targetVertex
        while node is not None:
            print "%s -> "%node.name
            node=node.predecessor

node1=vertex("A")
node2=vertex("B")
node3=vertex("C")

edge1=edge(1,node1,node2)
edge2=edge(1,node2,node3)
edge3=edge(2,node1,node3)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)

vertexList = {node1,node2,node3}
alg=Algorithm()
alg.calculateShortestPath(vertexList,node1)
alg.getShortestPathTo(node3)
