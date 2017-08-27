
#倒排索引类，完成快速查找功能

class InvertedIndex:
	def __init__(self):
		self.invertedIndex = {}

    #初始化倒排索引
	def initInvertedIndex(self,graph):
		for name in graph.vertexMap:
			vertex = graph.vertexMap[name].propert
			#遍历节点属性，为每个属性设置倒排索引
			for property in vertex:
				#print("%s  %s"%(property,vertex[property]))
				if property not in self.invertedIndex:
					arr = [vertex["_id"]]
					_type = vertex["_type"]
						
					property_dict = {}
					property_dict[vertex[str(property)]] = arr 
					self.invertedIndex[str(property)] = property_dict 
				else:
					if vertex[property] not in self.invertedIndex[property]:
						arr = [vertex["_id"]]
						self.invertedIndex[str(property)][vertex[str(property)]] = arr
					else:
						self.invertedIndex[str(property)][vertex[str(property)]].append(vertex["_id"])


	#解析查询语句
	def parseSql(self,sql):
		#example "name=xiaoming,age=27"
		conditions = []
		
		tokens = sql.split(',')
		for _sql in tokens:
			cond = []
			_tokens = _sql.split('=')
			if len(_tokens) != 2:
				print("condition error!")
				continue
			cond.append(_tokens[0])
			cond.append(_tokens[1])
			conditions.append(cond)
		return conditions
	
	#查询结果取交集，返回条件最终结果
	def intersec(self,arr):
		if len(arr) == 1:
			return arr[0]
		if len(arr) == 0:
			return []
		else:
			tmp_arr = arr[0]
			#遍历查询条件
			for _arr in arr:
				#查询结果取id的交集
				if len(_arr) == 0:
					return []
				tmp_arr = list(set(tmp_arr).intersection(set(_arr)))
		return tmp_arr

	#执行查询语句,返回当前条件下的ids
	def excSQL(self,sql,graph):
		self.initInvertedIndex(graph)
		_arr = []
		select_nodes = []

		conditions = self.parseSql(sql)
		for condition in conditions:
			type_key = condition[0]
			value_key = condition[1]
			#print(type_key,value_key)
			if type_key not in self.invertedIndex:
				print("%s property not exists" % (type_key))
				tmp_arr = []
				_arr.append(tmp_arr)
				continue
			else:
				if value_key not in self.invertedIndex[type_key]:
					print("type : %s, value : %s not exists" % (type_key,value_key))
					tmp_arr = []
					_arr.append(tmp_arr)
					continue
			tmp_arr = self.invertedIndex[str(type_key)][str(value_key)]

			_arr.append(tmp_arr)
		res_arr = self.intersec(_arr)

		for index in res_arr:
			#select_nodes.append(self.getVertex(i))
			select_nodes.append(graph.vertexMap[index].propert)
		return select_nodes


	