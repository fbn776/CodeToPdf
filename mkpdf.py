from fpdf import FPDF
import os


def get_pdfs(root: str, path_list: list[str], output: str):
    root = os.path.abspath(root)
    str = ""
    for item in path_list:
        rel_path = os.path.relpath(item, root)
        txt = read_file(item)
        file_name = os.path.basename(rel_path)
        loc_path = os.path.join(output, os.path.dirname(rel_path))

        str += read_file(file_name)
        # create_pdf(loc_path, file_name, txt)

    with open("Output.html", "w") as out:
        out.write(str)


def read_file(filename: str):
    with open(filename, "r") as f:
        return f.read()
