#!/bin/python

import os
import json

# Import Core_Config-Datei
with open('./lib/core_config.json', 'r') as file:
    core_config = json.load(file)

# Import Module Config
with open('./lib/modules/module_config.json', 'r') as file:
    module_config = json.load(file)
    
if not module_config['module']:
    print("NO MODULE SET")
    
else:    
    # List folder names in ./lib/versions/
    module_folders = [folder for folder in os.listdir('./lib/modules') if os.path.isdir(os.path.join('./lib/modules', folder))]
    
    sel_module = module_config['module']
    
    for module in module_folders:
        if module == sel_module:
            os.system(f'python ./lib/modules/{module}/{module}.py')