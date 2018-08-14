import os, json
import sys, os.path
from pprint import pprint

i = 0;
j = 1;

filesNum = 12;
totalAnnotationsProbe = 0;

basePath = os.path.dirname(__file__);

joinPath = os.path.join(os.path.dirname(__file__), '..', '..')
pathAbsPath = os.path.abspath(joinPath)

path_to_json = os.path.join(joinPath, 'dataset-samples', 'counters', '')

jsonListDir = os.listdir(path_to_json);
jsonFormat = pos_json.endswith('.json');

json_files = [pos_json for pos_json in jsonListDir if jsonFormat]

for i in range(filesNum):
  with open(path_to_json + json_files[i]) as f:
    data = json.load(f);
  for j in range(filesNum):
    with open(path_to_json + json_files[j]) as fCompare:
      dataCompare = json.load(fCompare);
    if data['rawData']['clinician'] == dataCompare['rawData']['clinician']:
      totalAnnotationProbe = totalAnnotationProbe + dataCompare['rawData']['time'];
    j = j + 1;
  print("The Total Annotations (Probe) of " + data['rawData']['clinician'] + " is ", totalAnnotationProbe);
  totalAnnotationProbe = 0;
  i = i + 1;