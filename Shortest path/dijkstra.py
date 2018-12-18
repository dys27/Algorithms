import sys
import heapq
class vertex(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor = None
        self.adjacencies_list=[]
        self.min_distance=sys.maxsize

    def __cmp__(self,other_vertex):
        return self.cmp(self.min_distance,other_vertex.min_distance)

    def __lt__(self,other):
        self_priority=self.min_distance
        other_priority=other.min_distance
        return self_priority<other_priority

class edge(object):
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight = weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex

class Algorithm(object):

    def calculate_shortest_path(self,vertex_list,start_vertex):
        queue=[]
        start_vertex.min_distance=0
        heapq.heappush(queue,start_vertex)

        while len(queue)>0:
            actual_vertex=heapq.heappop(queue)
   
            for edge in actual_vertex.adjacencies_list:
                u=edge.start_vertex
                v=edge.target_vertex
                new_distance=u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(queue,v)
    def get_shortest_path_to(self,target_vertex):
        print "Shortest path to target is: ",target_vertex.min_distance

        node=target_vertex
        while node is not None:
            print "%s -> "%node.name
            node=node.predecessor

node1=vertex("A")
node2=vertex("B")
node3=vertex("C")

edge1=edge(1,node1,node2)
edge2=edge(1,node2,node3)
edge3=edge(2,node1,node3)

node1.adjacencies_list.append(edge1)
node1.adjacencies_list.append(edge2)
node1.adjacencies_list.append(edge3)

vertex_list = {node1,node2,node3}
alg=Algorithm()
alg.calculate_shortest_path(vertex_list,node1)
alg.get_Shortest_path_to(node3)
