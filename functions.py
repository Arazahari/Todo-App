FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(filepath, todos_arg):
    with open(FILEPATH, 'w') as file:
        file.writelines(todos_arg)


print(type(__name__))
if __name__ != "__main__":
    pass
else:
    print("Hello")
    print(get_todos())
