import os
import io
import json
import itertools

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
		val = data["rawData"]["stacks"]
		#nameAndAnnotation[key] = nameAndAnnotationPairs.get(key,0) + val
		print(val)
print(nameAndAnnotationPairs)