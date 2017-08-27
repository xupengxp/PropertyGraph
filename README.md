1.PropertyGraph 实现了如下功能：

	1）.以json文件的形式导入边和定点信息，初始化图

	2）.提供查询顶点API，按照查询条件返回符合条件的顶点

	3）.提供最短路径计算API，指定图中任意两个顶点，返回最短路径及最短距离

2.文件结构：
	run.py             测试脚本 
	JasonReader.py     解析json
	Graph.py           保存图信息类
	Vertex.py          顶点类
	Edge.py            边类
	InvertedIndex.py   倒排索引类，实现条件查询
	Dijkstra.py        Dijkstra类，实现最短距离计算
	MinHeap.py         最小堆类，优化Dijkstra，参考博客：http://blog.csdn.net/desilting/article/details/44963419
	ini.jason          json文件，存储边和顶点信息

3.测试
	测试脚本参见run.py
	json = loadDataFromFile('data/ini.json')

	#初始化图
	graph = Graph()
	graph.iniGraph(json)

	#初始化Dijkstra
	dijk = Dijkstra()
	#测试最短距离查询，返回最短距离及其路径
	traversal_path,distince = dijk.minPath(graph,"2" ,"5") 
	print("the shortest path is : %s distince = %s \n" % (','.join(traversal_path),str(distince)))

	#初始化倒排索引
	invert = InvertedIndex()
	#按照条件查找，条件之间用','分隔，返回符合条件的顶点集合
	print("sql res : ")
	print(invert.excSQL("age=27,_type=person",graph))

	运行结果：
	the shortest path is : 2,6,4,5 distince = 0.9 

	sql res : 
	[{'name': 'xp', 'age': '27', '_id': '7', '_type': 'person'}, {'name': 'vadas', 'age': '27', '_id': '2', '_type': 'person'}, {'name': 'tt', 'age': '27', '_id': '1', '_type': 'person'}]