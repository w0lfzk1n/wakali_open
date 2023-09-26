#!/bin/python

import os
import questionary

def update_from_github(repo_url):
    # Ask for the version name
    version_name = questionary.text("Enter the name for this update version:").ask()
    version_path = os.path.join('./lib/versions', version_name)

    # Check if the version already exists
    if os.path.exists(version_path):
        print(f"Version {version_name} already exists!")
        return

    os.system(f'git clone {repo_url} {version_path}')
    print(f"\n\nUpdate {version_name} completed!")

# Update URL
# repo_url = "https://github.com/w0lfzk1n/wakali_open.git"
# update_from_github(repo_url)

print("\n\nUPDATE CURRENTLY NOT AVAILABLE")