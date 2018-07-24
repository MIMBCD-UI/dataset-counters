import os, json
import pandas as pd

timeCounter = 0;

path_to_json = '../../dataset-samples/counters/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)  # for me this prints ['foo.json']
