#pip install pysimplegui
import PySimpleGUI as sg
import conversion
sg.theme("DarkTeal2")
layout = [[sg.T("")],
          [sg.Text("Choose an Input folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],
          [sg.Text("Choose an Output folder: "), sg.Input(key="-IN3-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],
          [sg.Button("Submit"),sg.Button("Exit")]]

###Building Window
window = sg.Window('Malvern BOM Conversion', layout, size=(600,300))

while True:
    event, values = window.read()
    #print(values["-IN3-"])
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        conversion.main1(values["-IN2-"],values["-IN3-"])
        #filenames=conversion.filenameextract(directory_path)
        #dfupdated=conversion.dfallfiles(filenames,df_list)
        #dfupdated=conversion.mergedrows(dfupdated)
        #dfnew=conversion.atomconvert(dfupdated)
        #appended_df=conversion.formatting(dfnew)
        #conversion.outwrite(values["-IN3-"],appended_df)
        #conversion.flush()
        #conversion.outwrite(values["-IN3"])
        sg.popup("Task Completed Successfully")
window.close()



