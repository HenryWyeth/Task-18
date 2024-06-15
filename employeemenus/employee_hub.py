from employeemenus.employee_task_menu import employee_task_menu
from taskfunctions.specific_task_id import specific_task_id
from classes.task_library import task_library


def employee_hub():
    while True:
        print("\n===== Welcome back to the Employee Hub =====")
        menu_choice = input("\nHere you can:\n"
                            "1. Display all tasks in task library\n"
                            "2. Sort tasks by category\n"
                            "3. Search tasks by keyword\n"
                            "4. View an individual task\n"
                            "5. Log out\n"
                            "\nWhat action would you like to execute?\n")

        if "all" in menu_choice.lower():
            task_library.print_library()

        elif "sort" in menu_choice.lower():
            print("\n=== Sort Tasks ===\n")
            category_choice = input("\nBy which category do you wish to sort"
                                    " the task library?\n ('Title',"
                                    " 'Priority', 'Due Date', or 'Status')\n")
            task_library.sort_tasks(category_choice)

        elif "search" in menu_choice.lower():
            print("\n=== Search for Tasks===\n")
            keyword = input("\nPlease enter the keyword you wish to search:\n")
            task_library.search_tasks(keyword)

        elif "view" in menu_choice.lower():
            view_task = specific_task_id()
            employee_task_menu(view_task)

        elif "out" in menu_choice.lower():
            print("\n====== You are now logged out of the Wyeth Task"
                  " Management system =====")
            break
