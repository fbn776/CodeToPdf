from listReader import getFiles
from listGen import generateList

ROOT = "23BR15634"

path_list = generateList(ROOT)
getFiles(ROOT, path_list)
