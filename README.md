# Code to PDF

A command line python script that converts text files to pdfs; Specify the source directory, run the script, and voilà
the output PDFs are created and saved to the specified output (by default its `/output`).

## Why?

A util script, I made for converting the lab codes to pdf for record submission; 
The script was quickly put up for saving time. 
The original task was to convert about 75 students lab code each student had about 20+ exercises by hand.
This would've taken so much time, so I made this script to automate the process and has since saved a lot of time;


## Usage
Start by installing the dependencies;

```bash
pip install -r requirements.txt
```

Now you can run the script by;

```bash
python main.py <root-folder> [-i [--include] ...] [-o [--output]]
```


`root-folder`: The source folder to search for the text files to convert;
if found, this recursively finds all the file and converts them to PDFs

`-i` or `--include` [Optional]: Specifies the extensions to include when converting to PDF (space seperated).
If a file is found to not have the specified extension it is ignored.  

`-o` or `--output` [Optional]: Specifies the output location, by default its `/output`

For help, use
```bash
python main.py -h
```




## Example

Assume the folder structure is;
```
Lab/
├─ cycle1/
│  ├─ ex1.c
│  ├─ ex2.c
│  ├─ idk.cpp
│  ├─ temp.html
├─ cycle2/
│  ├─ ex3.java
│  ├─ ex4.java
```
Execute;
```bash
python main.py Lab -o LabPdfs -i c java
```

This creates pdfs for all file with the extensions `c`, `java` in source folder `Lab` and outputs the result to `LabPdfs`

```
Lab/
├─ cycle1/
│  ├─ ex1.c
│  ├─ ex2.c
│  ├─ idk.cpp
│  ├─ temp.html
├─ cycle2/
│  ├─ ex3.java
│  ├─ ex4.java

LabPdfs/
├─ cycle1/
│  ├─ ex1.pdf
│  ├─ ex2.pdf
├─ cycle2/
│  ├─ ex3.pdf
│  ├─ ex4.pdf
```

