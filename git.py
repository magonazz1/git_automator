#!/usr/bin/python3

import subprocess

def auto_git():
    """
    This function automates the process of staging, committing, and pushing Git changes.
    It prompts the user for a commit message.
    """
    # Adding all changes to the staging area
    subprocess.run(["git", "add", "."])

    # Prompting the user for a commit message
    commit_mesg = input("Write your commit message: ")

    # Committing the changes with the provided message
    subprocess.run(["git", "commit", "-m", commit_mesg])

    # Pushing the changes to the remote repository
    subprocess.run(["git", "push"])

def executable_check():
    """
    This function checks if the user's .py files have been made executable.
    If they have not, the program will make them executable.
    """
    user_prompt = input("""
    Have you made your .py executable?
    Type 'y' for Yes or 'n' for No:
    """)
    return (user_prompt)

def gito(user_prompt):
    """
    This function either performs a Git operation (auto_git) or makes Python files executable
    based on the user's input (yes or no).
    """
    if user_prompt.upper() == 'Y':
        auto_git()

    elif user_prompt.upper() == 'N':

        # Making all Python files executable
        subprocess.run("chmod +x *.py", shell=True)
    else:
        print("Invalid choice. Please enter 'y' for Yes or 'n' for No.")

if __name__ == "__main__":
    user_prompt = executable_check()
    gito(user_prompt)
