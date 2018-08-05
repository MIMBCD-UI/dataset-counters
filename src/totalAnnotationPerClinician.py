import os
import io
import json
import itertools
from string import Template

# The current folder path.
basePath = os.path.dirname(__file__)
# The path to the repository "root" folder.
joinPath = os.path.join(basePath, '..', '..')
pathAbsPath = os.path.abspath(joinPath)
# The path for the "dataset-samples" repository and "counters" folder.
path_to_json = os.path.join(pathAbsPath, 'dataset-samples', 'counters', '')
# Get all the JSON files inside the "counters" folder of
# "dataset-samples" repository.
json_files = [
  pos_json for pos_json in os.listdir(path_to_json)
  if pos_json.endswith('.json')
]
nameAndAnnotationPairs={}
for fileName in json_files:
	with io.open(path_to_json + fileName, "r") as f:
		data = json.load(f)
		key = data["rawData"]["clinician"]
		val=0
		for  i in   range(len(data["rawData"]["stacks"])):
			print (len(data["rawData"]["stacks"]))
			if string.find(data["rawData"]["stacks"][i],"freehand") >-1 :
				
					
					val= val+len(data["rawData"]["stacks"][i]["freehand"]["handles"]) 
					print (key + val)
			
			#for j in range(len(data[i])):
				#print(data[i][j])
				#for k in range(len(data[i][j])):
					#print(data[i][j][k])
				
					#return val = val + len(data["rawData"]["stacks"][2]["freehand"][0]["handles"])
			
		#while data["rawData"]["stacks"][2]["freehand"][0]["handles"][i]["x"] isinstance (x):
		
		#val = len(data["rawData"]["stacks"][2]["freehand"][0]["handles"])
		#val = data["rawData"]["stacks"][0]["freehand"][0]["handles"][0]
		#nameAndAnnotation[key] = nameAndAnnotationPairs.get(key,0) + val
		#print(val)
print(nameAndAnnotationPairs)


