# RAW BOM - BOM Conversion
* RAW BOM - BOM Conversion is a Python project to automatically convert the RAW BOM file into ATOM BOM template. 


# Execution
## RAW BOM to ATOM BOM (Directory)
1. Run the main-directoryname.py file
2. Provide the input and output directory path in CLI 
3. Converted ATOM BOM files will be available in the chosen output folder

## RAW BOM to ATOM BOM (File)
1. Run the main-filename.py file
2. Provide the input file path and output directory path in CLI. Output directory path is optional
   (eg: python main-filename.py E:\Format1.xlsx -o E:\output)
3. Converted ATOM BOM files will be available in the chosen output folder

#### Note
* For Format 7, and 10 : header has to be modified

* Python interpreter that comes pre-installed on Ubuntu Linux  has no support          for Tkinter.
Code to install python GUI Tkinkter module:

<code snippet>
sudo apt-get install python3-tk




