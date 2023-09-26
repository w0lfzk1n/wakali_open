#!/bin/python

# ===========================================
# Skriptname: WaKali.py
# Aufruf: python3 /WaKali.py
# Beschreibung: Kali implementation for Messenger
# Ersteller: Wolf & Sh8co
# Version: 0.01 dev-release
# Versionsdatum: 26.09.2024
# ===========================================

try:
    from subprocess import call
    import os
    import datetime
    import questionary
    import json
except ImportError:
    print("Some required modules are not installed, would you like to install them? (y/n)")
    answer = input("Choice:")
    if answer == 'y':
        print("   Installing Moduls...\nYou can ignore the most of the errors, they are just warnings.\nMay you have to install pip manually.")
        import pip
        pip.main(['install', 'json'])
        pip.main(['install', 'questionary'])
        pip.main(['install', 'subprocess'])
        print("\n\n>> MODULES INSTALLED! RESTART SCRIPT <<")
        exit()
    else:
        print("\n\nSCRIPT FAILED TO LAUNCH. MISSING LIBRARIES")

# Import Core_Config-Datei
with open('./lib/core_config.json', 'r') as file:
    core_config = json.load(file)

# Short function to clear console
def cl():
    if core_config['OS'] == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

run = True
try:
    while run:
        cl()
        choice = questionary.select(
            "**[ WaKali Menu ]**\n\n",
            choices=[
                'Start',
                'First Install',
                'Update',
                'Config',
                'Exit'
            ]).ask()
        
        if choice == 'Start':
            print("Starting Bot!")
            os.system('node ./lib/scripts/bot/index.js')
            
        elif choice == 'First Install':
            cl()
            print("First Install initiated!")
            os.system('python ./lib/scripts/install.py')
            
        elif choice == 'Update':
            cl()
            print("Update from GitHubRepo initiated!")
            os.system('python ./lib/scripts/update.py')
            
        elif choice == 'Config':
            cl()
            print("Edit core-configs!")
            os.system('python ./lib/scripts/edit_conf.py')
            
        elif choice == 'Exit':
            print("Programm terminated by user.")
            run = False
            break
except KeyboardInterrupt:
    run = False
    exit()
exit()
