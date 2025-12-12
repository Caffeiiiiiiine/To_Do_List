import csv


class Task:
    """
    Represents an individual task in the To-Do List.
    Attributes:
        name (str): Name of the task.
        description (str): Description of the task.
        priority (str): Priority of the task (High, Medium, Low).
    """
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Task(Name: {self.name}, Description: {self.description}, Priority: {self.priority})"


class ToDoList:
    """
    Manages the To-Do List and performs operations like adding, removing, viewing,
    saving to a CSV file, and loading from a CSV file.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task)
        print(f"Task '{task.name}' added successfully!")

    def remove_task(self, task_name):
        """Remove a task by name."""
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                self.tasks.remove(task)
                print(f"Task '{task.name}' removed successfully!")
                return
        print(f"Task '{task_name}' not found!")

    def view_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks found!")
        else:
            print("\nCurrent Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def save_to_csv(self, filename="tasks.csv"):
        """Save all tasks to a CSV file."""
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Description", "Priority"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])
        print(f"Tasks successfully saved to '{filename}'.")

    def load_from_csv(self, filename="tasks.csv"):
        """Load tasks from a CSV file."""
        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks = [
                    Task(row["Name"], row["Description"], row["Priority"]) for row in reader
                ]
            print(f"Tasks successfully loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty list.")


def display_menu():
    """Display the menu for the To-Do List application."""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Save Tasks to CSV")
    print("5. Load Tasks from CSV")
    print("6. Exit")


def main():
    """Main function to run the To-Do List application."""
    todo_list = ToDoList()
    todo_list.load_from_csv()  # Load tasks from CSV at startup if the file exists

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            priority = input("Enter task priority (High/Medium/Low): ").strip()
            if priority.lower() not in ["high", "medium", "low"]:
                print("Invalid priority! Please enter High, Medium, or Low.")
            else:
                task = Task(name, description, priority.capitalize())
                todo_list.add_task(task)

        elif choice == "2":
            task_name = input("Enter the name of the task to remove: ").strip()
            todo_list.remove_task(task_name)

        elif choice == "3":
            todo_list.view_tasks()

        elif choice == "4":
            todo_list.save_to_csv()

        elif choice == "5":
            todo_list.load_from_csv()

        elif choice == "6":
            print("Exiting To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()