class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        status = "Done" if self.done else "Pending"
        return f"{self.description} ({status})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()
            print("Task marked as done!")
        else:
            print("Invalid task number!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"'{removed_task.description}' removed from the list.")
        else:
            print("Invalid task number!")

    def menu(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Done")
            print("4. Remove Task")
            print("5. Exit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                description = input("Enter the task: ")
                self.add_task(description)
                print("Task added successfully!")
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks()
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                self.mark_task_done(task_index)
            elif choice == "4":
                self.view_tasks()
                task_index = int(input("Enter the task number to remove: ")) - 1
                self.remove_task(task_index)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.menu()
