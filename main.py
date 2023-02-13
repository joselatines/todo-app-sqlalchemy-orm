from db import session, Task
from uuid import uuid4


def add_task(task):
    try:
        id = str(uuid4())
        new_task = Task(id, task)
        session.add(new_task)
        session.commit()
        print("✅ Task added: ", task)
    except Exception:
        print("😨 Add a valid task")

    # tasks.append(task)


def view_tasks():
    try:
        tasks = session.query(Task)
        print("📚 Tasks:")
        for i, task in enumerate(tasks):
            print(i + 1, task.title)

        return True
    except Exception:
        print("😪 There no tasks. Add one!")
        # to not run any CRUD action
        return False


def complete_task(index):
    try:
        # This line sets index to 0 if it's an empty string, otherwise it's cast to an int
        index = int(0 if index == "" else index)

        tasks = session.query(Task)
        id = None
        for i, task in enumerate(tasks):
            if int(i + 1) == int(index):
                id = task.id
                break

        task_to_delete = session.query(Task).filter_by(id=id).one()
        session.delete(task_to_delete)
        session.commit()

        # task = tasks.pop(index - 1)
        print("✔️ Task completed: ", task.title)
    except:
        print("😨 Invalid task index.")


def run_app():
    while True:
        user_input = input("❓ Enter a command (add/view/complete/quit): ")
        user_input = user_input.upper()

        if user_input == "ADD":
            task = input("Enter a task: ")
            add_task(task)
        elif user_input == "VIEW":
            view_tasks()
        elif user_input == "COMPLETE":
            if view_tasks():
                index = input("✔️ Enter the task index to complete: ")

                complete_task(index)
        elif user_input == "QUIT":
            print("See you later! ✌")
            break
        else:
            print("😨 Invalid command.")


run_app()
