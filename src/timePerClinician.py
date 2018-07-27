#!/usr/bin/env python

"""

timePerClinician.py: Counting the total time per each Clinician on
                     a JSON files set.

"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "0.0.1"
__status__      = "Development"
__copyright__   = "Copyright 2018, Instituto Superior Técnico (IST)"
__credits__     = [
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes",
  "Duarte Figueirôa"
]

import os, json
import sys, os.path
from pprint import pprint

# Index variables of "for" loop.
i = 0
j = 1

# Insert manually the total number of files.
filesNum = 12

# Variable to recursively accumulate the total time number.
totalTime = 0

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

# Per each file "i". For instance, "i = 0" the first element
# will be the "1948.json" file.
for i in range(filesNum):
  # The following will iteratively read each JSON file. It starts
  # on the first ("i = 0") file of the folder.
  with open(path_to_json + json_files[i]) as f:
    data = json.load(f)
  # Per each file "j". For instance, "j = 1" the second element
  # will be the "1949.json" file.
  for j in range(filesNum):
    # The following will also iteratively read each JSON file. It starts
    # on the second ("j = 1") file of the folder.
    with open(path_to_json + json_files[j]) as fCompare:
      dataCompare = json.load(fCompare)
    # Comparing both "i = 0" with "j = 1" and see if the "clinician"
    # is the same between both files. If so, it sums the older time
    # with the new one.
    if data['rawData']['clinician'] == dataCompare['rawData']['clinician']:
      totalTime = totalTime + dataCompare['rawData']['time']
    j = j + 1
  clinicianName = data['rawData']['clinician']
  print("The Total Time of " + clinicianName + " is ", totalTime)
  totalTime = 0
  i = i + 1
