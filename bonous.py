import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Chose")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor", layout=[[label1,input1,choose_button],
                                              [label2,input2,choose_button2],
                                              [compress_button]])
window.read()
window.close()