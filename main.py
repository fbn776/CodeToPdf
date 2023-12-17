import os
import sys
import argparse
from mkpdf import get_pdfs
from list_gen import generate_files_list
import html
# CLI Arguments
parser = argparse.ArgumentParser()
parser.add_argument("root_folder", type=str, help="Name of the root folder that contains the file to convert")
parser.add_argument("-i", "--include", nargs="*", type=str,
                    help="File extensions to include when creating PDFs",
                    default=["txt", "py", "java", "c", "cpp", "html", "js"])
parser.add_argument("-o", "--output", type=str, help="Path to place the output file", default="output")
args = parser.parse_args()

# Config
ROOT = args.root_folder
include_exts = args.include
output_filename = args.output

# If `--include` starts with `.`, then remove it;
for i, j in enumerate(include_exts):
    if not j.startswith("."):
        include_exts[i] = "." + j

if not os.path.isdir(ROOT):
    print("Invalid root; root must be a present folder")
    sys.exit(2)

path_list = generate_files_list(ROOT, include_exts)

str = ""
for item in path_list:
    with open(item, "r") as f:
        str += f"""
            <h1 align="center">Title</h1>
            <h3>Aim:</h3>
            <h3>Algorithm:</h3>
            <h3>Program Development:</h3>
            <pre>{html.escape(f.read())}</pre>
            <h3>Output:</h3>
            <br/><div class="page-break"></div>
        """

with open(output_filename, "w") as f:
    f.write("""
        <html>
            <head>
                <style>
                    body {
                        font-size: 14px;
                    }
                    @media print {
                        .page-break {
                            page-break-before: always;
                        }
                    }
                </style>
            </head>
            <body>
    """ + str + """
            </body>
        </html>
    """)


print(f"Converted {len(path_list)} files to pdf")
