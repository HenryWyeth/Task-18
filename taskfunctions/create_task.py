import uuid
import re
from classes.task import Task
from classes.task_library import task_library


def create_task():
    """
    Creates a task instance and stores it in the task library.
    """
    print("\n=== Task Creator ===\n")
    # Generate a random UUID (UUID4)
    new_unique_id = str(uuid.uuid4())

    new_title = input("Task title: ")
    while new_title == "":
        print("Input Error: Please enter a title for this task.")
        new_title = input("Task title: ")

    new_priority = input("\nTask priority (High, Medium, Low): ")
    while (new_priority.lower() != "high" and
           new_priority.lower() != "medium" and
           new_priority.lower() != "low"):
        print("Input Error: Please type a choice from 'High', 'Medium', or"
              " 'Low'.")
        new_priority = input("\nTask priority (High, Medium, Low): ")

    new_due_date = input("\nTask due date (YYYY/MM/DD): ")
    while not re.match(r"^\d{4}/\d{2}/\d{2}$", new_due_date):
        print("Input Error: Please ensure your due date input matches the"
              " YYYY/MM/DD format.")
        new_due_date = input("\nTask due date (YYYY/MM/DD): ")

    new_status = input("\nTask status (Incomplete, Submitted for Review,"
                       " Completed): ")
    while (new_status.lower() != "incomplete" and
           new_status.lower() != "submitted for review" and
           new_status.lower() != "completed"):
        print("Input Error: Please type a choice from 'Incomplete', 'Submitted"
              " for Review', or 'Complete'.")
        new_status = input("\nTask status (Incomplete, Submitted for Review,"
                           " Completed): ")

    new_task = Task(new_unique_id, new_title, new_priority, new_due_date,
                    new_status)

    task_library.add_task(new_task)
