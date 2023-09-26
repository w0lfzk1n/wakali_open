#!/bin/python

import json
import questionary
import os

#Function to show config
def show_config(core_config):
    for key, value in core_config.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f"{sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

# Function to edit config
def edit_config(core_config):

    try:
        # Edit OS
        os_choice = questionary.select(
            "Choose your operating system:",
            choices=[
                f"Keep: {core_config['OS']}",
                'Windows',
                'Linux',
            ]).ask()

        if os_choice and not os_choice.startswith('Keep:'):
            core_config['OS'] = os_choice
    except KeyboardInterrupt:
        exit()

    try:
        # List folder names in ./lib/versions/
        version_folders = [folder for folder in os.listdir('./lib/versions') if os.path.isdir(os.path.join('./lib/versions', folder))]

        # Edit version
        version_choice = questionary.select(
            "Choose your project version:",
            choices=[
                f'Keep: {core_config["version"]}',
                *version_folders
            ]).ask()

        if version_choice and not version_choice.startswith('Keep:'):
            core_config['version'] = version_choice
    except KeyboardInterrupt:
        exit()

    try:
        # Edit project_path
        path_choice = questionary.select(
            "Set your project path:",
            choices=[
                f'Keep: {core_config["project_path"]}',
                'Current folder',
                'Custom',
            ]).ask()

        if path_choice == 'Current folder':
            core_config['project_path'] = os.getcwd()
        elif path_choice == 'Custom':
            while True:
                custom_path = questionary.text(f"Enter your custom path (ENTER to keep config):").ask()
                if custom_path:
                    if os.path.exists(custom_path):
                        core_config['project_path'] = custom_path
                        break
                    else:
                        print("The provided path does not exist. Please try again.")
                else:
                    break
    except KeyboardInterrupt:
        exit()

    try:
        # Edit Auth
        user = questionary.text(f"Enter your Username for auth (ENTER to keep user: {core_config['auth']['user']}):").ask()
        if user:
            core_config['auth']['user'] = user

        password = questionary.password(f"Enter your Password for auth (ENTER to keep current password):").ask()
        if password:
            core_config['auth']['pass'] = password

        # Save JSON file
        with open('./lib/core_config.json', 'w') as file:
            json.dump(core_config, file, indent=4)

        print("Config saved!")
    except KeyboardInterrupt:
        exit()


#   MENU
# Load JSON file
with open('./lib/core_config.json', 'r') as file:
    core_config = json.load(file)

if core_config['OS'] == 'Windows':
    os.system('cls')
else:
    os.system('clear')

while True:
    main_choice = questionary.select(
        "What would you like to do?",
        choices=[
            "Show Config",
            "Edit Config",
            "Exit"
        ]).ask()

    if main_choice == "Show Config":
        show_config(core_config)
    elif main_choice == "Edit Config":
        edit_config(core_config)
    elif main_choice == "Exit":
        break

