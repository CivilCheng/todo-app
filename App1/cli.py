import time
from functions import get_todos, write_todos

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

todos = get_todos()

user_prompt = "Type add, show, edit, complete, or exit:"

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4::] + '\n'
        todos.append(todo)

    elif user_action.startswith("show"):
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.capitalize()
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5::])
            number -= 1
            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

        except ValueError:
            print("Your command is not valid")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9::])
            todo_to_remove = todos.pop(number - 1)
            todo_to_remove = todo_to_remove.strip('\n')
            print(f"Todo {todo_to_remove} was removed from the list.")

        except IndexError:
            print("Your command is not valid")

    elif user_action.startswith("exit"):
        break
    else:
        print("Entered an unknown command")

write_todos(todos, 'todos.txt')

print("Bye")
