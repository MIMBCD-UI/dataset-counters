#!/usr/bin/env python

"""

totalTime.py: Counting the total time of a JSON files set.

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

timeCounter = 0;
i = 0;
filesNum = 12;
totalTime = 0;

joinPath = os.path.join(os.path.dirname(__file__), '..', '..')
pathAbsPath = os.path.abspath(joinPath)

path_to_json = os.path.join(joinPath, 'dataset-samples', 'counters', '')

json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

while i < filesNum:
  with open(path_to_json + json_files[i]) as f:
    data = json.load(f)
  i = i + 1
  totalTime = totalTime + data["rawData"]["time"]

print(totalTime)
