from functions import get_todos, write_todos
import time
todos = []

now = time.strftime('%b %d, %Y %H:%M:%S')
print("It is",now)
while True:
    user_action = input('Enter add, show, edit,complete or exit:').strip()
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos('todos.txt', todos_arg)

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f'{index + 1}-{item}')
        print(len(todos))
    elif user_action.startswith('edit'):
        try:

            number = int(user_action[5:])
            number = number - 1
            print(number)

            get_todos()

            new_todo = input('add new one')
            todos[number] = new_todo + '\n'

            write_todos('todos.txt', todos_arg)

        except ValueError:
            print('Your command is not valid.')
            continue
    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('complete'):
        try:

            number = int(user_action[9:])
            number = number - 1
            todos = get_todos()
            todos.pop(number)
            write_todos('todos.txt', todos_arg)
        except IndexError:
            print('Number that you entered is not valid.')

    else:
        print('Command is not valid.')

print('Bye')
