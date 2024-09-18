class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\nTo-Do List Application")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Update a task")
        print("4. Remove a task")
        print("5. Quit")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks to show.")
            return

        print("\nTasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def add_task(self):
        task = input("\nEnter a new task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def update_task(self):
        if not self.tasks:
            print("\nNo tasks to update.")
            return

        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(self.tasks):
                new_task = input("Enter the new task: ")
                self.tasks[task_number - 1] = new_task
                print(f"Task {task_number} updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def remove_task(self):
        if not self.tasks:
            print("\nNo tasks to remove.")
            return

        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                print("Exiting the To-Do List application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
