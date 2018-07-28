import os, json
from pprint import pprint

timeCounter = 0;
i = 0;
filesNum = 12;
totalTime = 0;

path_to_json = '../../dataset-samples/counters/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

while i < filesNum:
  with open(path_to_json + json_files[i]) as f:
    data = json.load(f)
  i = i + 1
  totalTime = totalTime + data["rawData"]["time"]
  
pprint(totalTime)