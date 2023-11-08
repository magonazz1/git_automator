# Git Automator

This project is a Python script that provides two main features:

1. **Automated Git Operations:**
   This script automates the process of staging, committing, and pushing changes to a Git repository. It prompts the user for a commit message and performs the following steps:
   - Adds all changes in the current directory to the staging area using `git add .`.
   - Prompts the user to provide a commit message.
   - Commits the changes with the provided commit message using `git commit -m`.
   - Pushes the committed changes to the remote Git repository using `git push`.

2. **Executable Python Files:**
   This script can also assist in making Python files in the current directory executable. It checks if the user's .py files have been made executable. If not, it makes them executable using the `chmod +x *.py` command.

## Usage

To use this script, follow these steps:

## Prerequisite
To make use of this tool, a few prerequisites are assumed:

- You are expected to have an existing Git repository where you are actively working. This repository should contain a collection of files, which may include Python files or any other files written in your chosen programming language.

- Additionally, it is assumed that you have already configured your global Git settings, particularly `user.name` and `user.email`, to match the settings associated with the Git repository where your files reside.

- Before proceeding to clone and use this tool, it is essential that you navigate to the directory of your existing repository, the location where your files are stored.

By ensuring that these prerequisites are met, you can effectively use this tool within the context of your project.

Here are the steps to use the tool

1. **Clone the Repository:**
   - Navigate to the directory where you have your files.
   - Clone this repository by running the following command:
     ```bash
     git clone https://github.com/magonazz1/git_automator.git && cd git_automator && ./start && cd .. && rm -rf git_automator
     ```
   - After running the command, you can check if the "gito" file has appeared in your current directory by using the `ls` command.

2. **Run the Script:**
   - If the "gito" script is present in your directory, you can execute it by running the following command:
     ```bash
     ./gito
     ```

3. **Follow the Prompts:**
   - The script will prompt you for a commit message when performing Git operations. Enter your desired commit message as instructed.

4. **Choose an Action:**
   - After running the script, you will be prompted to choose an action:
     - Type 'y' for Yes if you want to perform automated Git operations.
     - Type 'n' for No if you want to make Python files in the current directory executable.

## Room for Improvement

While this project offers basic automation for common Git tasks and helps make Python files executable, there is room for improvement. Here are some potential enhancements:

1. **Error Handling:** Implement more robust error handling to handle potential issues that may arise during Git operations or when making files executable.

2. **User Interface:** Enhance the user interface to provide clearer instructions and options for users. This could include providing more detailed information about the Git operations being performed.

3. **Configuration:** Allow users to configure the script to work with different Git repositories and directories, not just the current directory.

4. **Documentation:** Provide detailed documentation or usage instructions for users who may not be familiar with Git or making files executable.

5. **Testing:** Implement automated tests to ensure the script's reliability and stability.

## Open Source - Project

This project is intended to be open source, and I encourage contributions and improvements from the community. Feel free to fork the repository, make enhancements, and submit pull requests. Let's work together to make this tool even more useful.

**Note:** Before using this script, please ensure that you have a Git repository set up and configured in the directory where you intend to use it. Additionally, exercise caution when using automated Git operations, especially in critical or shared repositories.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/magonazz1/git_automator/blob/master/LICENSE) file for details.
