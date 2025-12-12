⚙️ Installation & Setup Guide
This guide covers how to set up your development environment using Conda and PyBullet on VS Code. These steps work for Windows and Linux, and are specifically tested for macOS.

1. Install Conda (Miniconda)
We recommend using Miniconda (a lightweight version of Anaconda) to manage your Python environments.

Download: Go to the Miniconda Official Site and download the installer for your OS (select "macOS pkg" for Mac).

Install: Run the installer and follow the prompts.

Verify: Open your terminal (or Command Prompt) and type:

Bash

conda --version
2. Create a Virtual Environment
Important: Never install packages globally! Create an isolated environment for this project.

Create the environment (we'll call it drone_env and use Python 3.8, which is stable for PyBullet):

Bash

conda create --name drone_env python=3.8
Activate the environment:

Bash

conda activate drone_env
3. Install PyBullet
With your environment activated, install the physics engine:

Bash

pip install pybullet numpy
Note for macOS Users: If you encounter issues on Apple Silicon (M1/M2 chips), ensure you have Rosetta installed or try installing via Conda:

Bash

conda install -c conda-forge pybullet
4. Setting up VS Code
Install the Extension: Open VS Code, go to the Extensions tab (square icon on the left), and install the Python extension by Microsoft.

Select Interpreter:

Open your python file (e.g., main.py).

Press Cmd + Shift + P (Mac) or Ctrl + Shift + P (Windows) to open the Command Palette.

Type and select: Python: Select Interpreter.

Look for the one named drone_env (it usually says ('drone_env': conda)).

📚 References & Troubleshooting
PyBullet Quickstart Guide

VS Code Python Setup

Conda Cheat Sheet

🐙 Git & GitHub Commands Cheat Sheet
Here is a breakdown of the essential commands to get your code from your laptop to GitHub.

1. Initialize a Repository
Scenario: You have a folder on your computer, but it's not a Git repo yet.

Bash

git init
Function: Turns the current folder into a Git repository (creates a hidden .git folder).

2. Stage Changes
Scenario: You made changes (e.g., created main.py), and you want to prepare them for saving.

Bash

git add .
Function: Moves all changed files from your "Working Directory" to the "Staging Area".

Variant: git add filename.py (adds only one specific file).

3. Commit (Save)
Scenario: Your files are staged, and you want to save a snapshot of this version.

Bash

git commit -m "Initial commit"
Function: Takes everything in the Staging Area and saves it to the local history with a message describing what you did.

4. Branching
Scenario: You want to ensure you are on the main branch (standard naming).

Bash

git branch -M main
Function: Renames your current branch to main.

5. Link to GitHub (Remote)
Scenario: You created a new empty repository on GitHub.com and want to connect your local folder to it.

Bash

git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
Function: Tells your local git that "origin" is the URL of your cloud repository. It creates a bridge between your computer and GitHub.

6. Push (Upload)
Scenario: You want to send your local commits to GitHub.

Bash

git push -u origin main
Function: Uploads your code to the main branch of the origin (GitHub).

Note: The -u flag saves this setting, so next time you can just type git push.

Summary Workflow
When you make changes tomorrow, the flow is simpler:

Bash

git add .                                # 1. Stage
git commit -m "Fixed drone altitude bug" # 2. Save
git push                                 # 3. Upload