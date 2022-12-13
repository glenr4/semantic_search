import os


def setWorkingToCurrentFile():
    print(os.getcwd())
    print(__file__)
    filePath = os.path.dirname(__file__)
    print(filePath)

    if filePath != '':
        print("Changing working directory")
        os.chdir(filePath)
        print(os.getcwd())
