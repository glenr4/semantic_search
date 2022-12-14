import os

# Useful for changing working directory for VSCode debugger


def setWorkingToCurrentFile():
    filePath = os.path.dirname(__file__)

    if filePath != '':
        os.chdir(filePath)

    print(f'Working directory is: {os.getcwd()}')
