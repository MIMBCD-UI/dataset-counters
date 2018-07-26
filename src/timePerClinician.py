import os, json
import sys, os.path
from pprint import pprint

i = 0;
j = 1;

timeCounter = 0;
filesNum = 12;
totalTime = 0;
doctorTime = 1;

joinPath = os.path.join(os.path.dirname(__file__), '..', '..')
pathAbsPath = os.path.abspath(joinPath)

path_to_json = os.path.join(joinPath, 'dataset-samples', 'counters', '')

json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for i in range(filesNum):
  with open(path_to_json + json_files[i]) as f:
    data = json.load(f);
  for j in range(filesNum):
    with open(path_to_json + json_files[j]) as fCompare:
      dataCompare = json.load(fCompare);
    if data['rawData']['clinician'] == dataCompare['rawData']['clinician']:
      totalTime = totalTime + dataCompare['rawData']['time'];
    j = j + 1;
  print("The Total Time of " + data['rawData']['clinician'] + " is ", totalTime);
  totalTime = 0;
  i = i + 1;
