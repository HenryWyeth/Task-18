import re


def update_task(task):
    print("\n===== Update Task =====\n")
    yes_no = input("Are you sure you would like to update this"
                   " task?\n")
    if "yes" in yes_no.lower():
        attribute = input("Which of the task's attributes would you"
                          " like to update?\n 'Title', 'Priority', 'Due Date',"
                          " or 'Status'\n")
        if "title" in attribute.lower():
            attribute = "title"

        elif "priority" in attribute.lower():
            attribute = "priority"

        elif "due date" in attribute.lower():
            attribute = "due_date"

        elif "status" in attribute.lower():
            attribute = "status"

        else:
            print("Input Error: Please select a valid attribute.")
            attribute = input("Which of the task's attributes would you"
                              " like to update?\n 'Title', 'Priority',"
                              " 'Due Date', or 'Status'\n")

        new_value = input("What new value would you like to give to"
                          f" {attribute}?\n")

        if attribute.lower() == "priority":
            while (new_value.lower() != "high" and
                   new_value.lower() != "medium" and
                   new_value.lower() != "low"):
                print("Input Error: Please type a choice from 'High',"
                      " 'Medium', or 'Low'.")
                new_value = input("\nTask priority (High, Medium, Low): ")

        elif attribute.lower() == "due_date":
            while not re.match(r"^\d{4}/\d{2}/\d{2}$", new_value):
                print("Input Error: Please ensure your due date input matches"
                      " the YYYY/MM/DD format.")
                new_value = input("\nTask due date (YYYY/MM/DD): ")

        elif attribute.lower() == "status":
            while (new_value.lower() != "incomplete" and
                   new_value.lower() != "submitted for review" and
                   new_value.lower() != "completed"):
                print("Input Error: Please type a choice from 'Incomplete',"
                      "'Submitted for Review', or 'Complete'.")
                new_value = input("\nTask status (Incomplete, Submitted for"
                                  " Review, Completed): ")

        task.update_task(attribute.lower(), new_value)
