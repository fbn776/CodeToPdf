import os


def generateList(root: str):
    """
    Takes in a root path and returns a list of absolute path of all the .java and .c files in that folder recursively
    :param root: The root path
    :return: List of absolute path of all c and java file in root
    """
    path_list: list[str] = []
    os.chdir(root)
    contents = os.listdir()

    for item in contents:
        # Check if the listed items is a folder and not hidden one;
        if os.path.isdir(item) and not item.startswith("."):
            # Get into the folder
            os.chdir(item)
            sub_contents = os.listdir()
            for sub_item in sub_contents:
                appendFilePath(sub_item, path_list)
            # Get out of the folder
            os.chdir("../")
    os.chdir("../")

    return path_list


def appendFilePath(sub: str, path_list: list[str]):
    """
    This is the recursive function that goes through each file and appends the abs path
    """
    if os.path.isdir(sub):
        os.chdir(sub)
        items = os.listdir()
        for i in items:
            appendFilePath(i, path_list)
        os.chdir("../")
    else:
        if not sub.endswith(".c") and not sub.endswith(".java"):
            return

        path_list.append(os.path.abspath(sub))