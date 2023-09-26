#!/bin/python

import os
import json

# Import Core_Config-Datei
with open('./lib/core_config.json', 'r') as file:
    core_config = json.load(file)

# Import Module Config
with open('./lib/modules/module_config.json', 'r') as file:
    nmap_config = json.load(file)
