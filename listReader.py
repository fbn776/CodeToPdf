from fpdf import FPDF
import os


def create_pdf(save_loc: str, filename: str, text: str):
    pdf = FPDF()
    pdf.add_page()

    # Set font and position
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 5, txt=text, align="L")

    # Check if directory exists, create it if not
    if not os.path.exists(save_loc):
        os.makedirs(save_loc)

    last_dot_index = filename.rindex(".")

    # f = open(os.path.join(save_loc, filename[:last_dot_index] + ".pdf"), "wb")
    # f.write(output)
    pdf.output(os.path.join(save_loc, filename[:last_dot_index] + ".pdf"))


def getFiles(root: str, path_list: list[str]):
    root = os.path.abspath(root)
    for item in path_list:
        rel_path = os.path.relpath(item, root)
        txt = readFile(item)
        file_name = os.path.basename(rel_path)
        loc_path = os.path.join("output", os.path.dirname(rel_path))

        create_pdf(loc_path, file_name, txt)


def readFile(filename: str):
    with open(filename, "r") as f:
        return f.read()
