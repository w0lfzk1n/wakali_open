
import json
import questionary
import os

# Load Core_Config
with open('./lib/core_config.json', 'r') as file:
    core_config = json.load(file)
    
if core_config['OS'] == 'Windows':
    os.system('cls')
else:
    os.system('clear')

try:
    if not core_config['OS']:
        os_choice = questionary.select(
            "Choose your operating system:",
            choices=[
                'Windows',
                'Linux',
            ]).ask()
        core_config['OS'] = os_choice

    # Save JSON file
    with open('./lib/core_config.json', 'w') as file:
        json.dump(core_config, file, indent=4)
    
except KeyboardInterrupt:
    exit()