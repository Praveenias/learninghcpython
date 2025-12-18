#pip install pysimplegui
import PySimpleGUI as sg
import main
#sg.theme("DarkTeal2")
layout = [[sg.T("")],
          [sg.Text("Choose an Input folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],
          [sg.Text("Choose an Output folder: "), sg.Input(key="-IN3-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],
          [sg.Button("Submit",pad=(50, 50)), sg.Button("Validate",size=(10, 2),pad=(90, 90)), sg.Button("Exit",size=(10, 1),pad=(50, 50))]]

###Building Window
window = sg.Window('Thermofisher BOM Conversion', layout, size=(600,300))

while True:
    event, values = window.read()
    #print(values["-IN3-"])
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        main.main1(values["-IN2-"],values["-IN3-"])
        sg.popup("Task Completed Successfully")
    elif event == "Validate":
        main.main2(values["-IN2-"],values["-IN3-"])
        sg.popup("Validation Completed Successfully")
window.close()



