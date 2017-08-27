from Vertex import *
from Edge import *
import math


class Graph:

    def __init__(self):
        self.vertexMap = {}                   #存储所有边和顶点信息


    def iniGraph(self,json):
        vertex_dic = {}                      

        #遍历json文件中顶点信息
        for vert in json["vertices"]:
            index = vert["_id"]
            vertex_dic[index] = vert 

        #遍历json文件中边信息
        for vertex in json["edges"]:
            sourceName = vertex["_outV"]
            destinationName = vertex["_inV"]
            weight = vertex["weight"]
            relation = vertex["relation"]
            self.addEdge(sourceName,destinationName,weight,relation,vertex_dic)

    #添加边信息，同时初始化顶点
    def addEdge(self, sourceName, destinationName, weight,relation ,vertex_dic):
        source = self.getVertex(sourceName, vertex_dic[sourceName], createNew=True)
        destination = self.getVertex(destinationName, vertex_dic[destinationName], createNew=True)
        source.addEdge(Edges(source, destination, float(weight),relation))
        destination.addEdge(Edges(destination, source, float(weight),relation))

    #初始化顶点
    def getVertex(self, vertexName, propert, createNew=False ):
        try:
            v = self.vertexMap.get(vertexName)
            if v is None and createNew:
                v = Vertex(vertexName,propert)
                self.vertexMap[vertexName] = v
            return v
        except KeyError as e:
            print("Exception ", e)

    def addVertex(self, vertexName):
        self.getVertex(vertexName, createNew=True)


    def __len__(self):
        return len(self.vertexMap)