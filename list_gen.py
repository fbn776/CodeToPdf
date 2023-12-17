import os


def generate_files_list(root: str, include_exts: list[str]):
    """
    Takes in a root path and returns a list of absolute path of all the files with specified extensions [include] in
    that folder recursively
    :param include_exts: A list of extensions to be included
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
                append_file_path(sub_item, path_list, include_exts)
            # Get out of the folder
            os.chdir("../")
        else:
            append_file_path(item, path_list, include_exts)

    os.chdir("../")

    return path_list


def append_file_path(sub: str, path_list: list[str], include_exts: list[str]):
    """
    This is the recursive function that goes through each file and appends the absolute path to the given path_list ref
    :param sub: Current subdirectory or file
    :param path_list: The reference of path list array, paths are appended to this array
    :param include_exts: File extensions to include
    """
    if os.path.isdir(sub):
        os.chdir(sub)
        items = os.listdir()
        for i in items:
            append_file_path(i, path_list, include_exts)
        os.chdir("../")
    else:
        lsub = sub.lower()
        # Only include files that has the specified extensions
        for i in include_exts:
            if lsub.endswith(i.lower()):
                path_list.append(os.path.abspath(sub))
                return
