import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('DarkGreen6')
clock = sg.Text("", key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button(image_source='004 add.png', tooltip="Add",
                       mouseover_colors='LightBlue2,', key='Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True,size=(40,10))
complete_button = sg.Button(image_source='004 complete.png',
                            tooltip='Complete',
                            mouseover_colors='LightBlue2',
                            key='Complete')
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
layout = ([clock], [label], [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button])
window = sg.Window("My To-Do App",
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=150)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(event)
    print(values)
    print(values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos('todos.txt', todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select Something")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos('todos.txt', todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please Select Something")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()
