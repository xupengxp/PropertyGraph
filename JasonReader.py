import os
import json

###load data from json file
def loadDataFromFile(path):
	with open(path) as json_file:
		data = json.load(json_file)
		return data