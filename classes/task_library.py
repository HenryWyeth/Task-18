import uuid
from random import choice, randint
from classes.task import Task


class TaskLibrary:
    def __init__(self) -> None:
        self.task_library = {}

    def add_task(self, task):
        self.task_library[task.unique_id] = task

    def get_task(self, unique_id):
        task = self.task_library.get(unique_id)
        return task

    def print_library(self):
        """
        Show entire task library contents.
        """
        if self.task_library:
            print("\n===== All Tasks =====\n")
            for task_idx, task in enumerate(self.task_library.values(),
                                            start=1):
                print(f"\n=== Task {task_idx}: ===")
                task.view()
        else:
            print("\n===== Task Library Empty ======\n")

    def print_task(self, unique_id):
        task = self.task_library.get(unique_id)
        if task:
            task.view()
        else:
            print(f"No task found in library with the Unique ID: {unique_id}")

    def pending_review(self):
        """
        Show all tasks waiting to be reviewed.
        """
        print("\n===== Tasks Awaiting Review =====\n")
        for task_idx, (task_id, task) in enumerate(self.task_library.items(),
                                                   start=1):
            if task.status == "Submitted for Review":
                print(f"=== Task {task_idx}: ===")
                task.view()
                print("-" * 20)

    def search_tasks(self, keyword):
        """
        Search for tasks by a specific keyword in their title.
        """
        matching_tasks = []
        for task_id, task in self.task_library.items():
            if keyword.lower() in task.title.lower():
                matching_tasks.append(task)

        if matching_tasks:
            print(f"\n===== Tasks containing '{keyword}' in their title"
                  " =====\n")
            for task in matching_tasks:
                task.view()
                print("-" * 20)
        else:
            print(f"\nNo tasks found in library with '{keyword}' in their"
                  " title.\n")

    def sort_tasks(self, category):
        """
        Sorts the task library depending on user specified category.
        """
        sorted_tasks = None
        if category.lower() == "title":
            sorted_tasks = sorted(self.task_library.values(),
                                  key=lambda task: task.title.lower())
        elif category.lower() == "priority":
            sorted_tasks = sorted(self.task_library.values(),
                                  key=lambda task: task.priority.lower())
        elif category.lower() == "due date":
            sorted_tasks = sorted(self.task_library.values(),
                                  key=lambda task: task.due_date.lower())
        elif category.lower() == "status":
            sorted_tasks = sorted(self.task_library.values(),
                                  key=lambda task: task.status.lower())
        else:
            print("Invalid sorting category. Please choose from 'Title',"
                  " 'Priority', 'Due Date', or 'Status'.")
            return

        print("\n===== All Tasks =====\n")
        for task_idx, task in enumerate(sorted_tasks, start=1):
            print(f"=== Task {task_idx} ===\n")
            task.view()
            print("-" * 20)

    def delete_task(self, unique_id):
        if unique_id.lower() not in self.task_library:
            print(f"No task found in library with the Unique ID: {unique_id}")

        else:
            confirm_delete = input("\nAre you sure you want to delete this"
                                   " task?\n")
            if "yes" in confirm_delete.lower():
                del self.task_library[unique_id.lower()]
                print("\nTask deleted successfully!\n")
            else:
                print("\nTask deletion cancelled.\n")


def random_task_generation(num_tasks):
    """
    Generating some random tasks to showcase the software for the purposes
    of this exercise.
    """
    example_titles = ["Fulfil order",
                      "Mow the lawn",
                      "Create presentation slide-deck",
                      "Respond to client proposal"]
    example_priority = ["High", "Medium", "Low"]
    example_status = ["Incomplete", "Submitted for Review",
                      "Complete"]

    for _ in range(num_tasks):
        unique_id = str(uuid.uuid4())
        title = choice(example_titles)
        priority = choice(example_priority)
        due_date = f"2024/{randint(1, 12):02d}/{randint(1, 31):02d}"
        status = choice(example_status)

        task_library.add_task(Task(unique_id, title, priority, due_date,
                                   status))


task_library = TaskLibrary()
