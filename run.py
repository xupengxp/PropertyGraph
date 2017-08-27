from Dijkstra import Dijkstra
from Graph import Graph
from JasonReader import *
from InvertedIndex import*

#读取json文件
json = loadDataFromFile('data/ini.json')

#初始化图
graph = Graph()
graph.iniGraph(json)

#初始化Dijkstra
dijk = Dijkstra()
#测试最短距离查询，返回最短距离及其路径
traversal_path,distince = dijk.minPath(graph,"2" ,"5") 
#print(traversal_path,distince)
print("the shortest path is : %s distince = %s \n" % (','.join(traversal_path),str(distince)))

#初始化倒排索引
invert = InvertedIndex()
#按照条件查找，条件之间用','分隔，返回符合条件的顶点集合
print("sql res : ")
print(invert.excSQL("age=27,_type=person",graph))

