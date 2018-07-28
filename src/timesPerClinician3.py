#!/usr/bin/env python

"""

timePerClinician3.py: Counting the total time per each Clinician on
                      a JSON files set.

"""

__author__      = "Bruno Oliveira"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "0.0.1"
__status__      = "Development"
__copyright__   = "Copyright 2018, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira"
]

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

nameAndTimePairs={}
for fileName in json_files:
	f = io.open(path_to_json + fileName, "r")
	data = json.load(f)
	key = data["rawData"]["clinician"]
	val = data["rawData"]["time"]
	nameAndTimePairs.update({key:nameAndTimePairs.get(key,0)+val})

print(nameAndTimePairs)
