# Raw BOM - Atom Bom Conversion and Validation
* Raw BOM - Atom Bom Conversion and Validation is a Python project to automatically convert the RAW BOM file into ATOM BOM template. 
* The project also includes a validate feature to check and validate if all details in RAW BOM is available in ATOM BOM.

# Execution
## RAW BOM to ATOM BOM
1. Run the Graphics.py file
2. Provide the input and output directory path 
3. Click Submit Button
4. Code execution concludes with Task Completed Successfully Message
5. Converted ATOM BOM files will be available in the chosen output folder
## ATOM BOM Validation
1. Run the Graphics.py file
2. Provide the input and output (with converted files) directory path 
3. Click Validate Button
4. Code execution concludes with Task Completed Successfully Message
5. Validation results will be added in corresponding output files on a new sheet titled "IPN_Match Status"
#### Note
* For Format 7, and 10 : header has to be modified

* Python interpreter that comes pre-installed on Ubuntu Linux  has no support          for Tkinter.
Code to install python GUI Tkinkter module:

<code snippet>
sudo apt-get install python3-tk




