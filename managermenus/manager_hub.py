from taskfunctions.create_task import create_task
from taskfunctions.import_task import import_task
from taskfunctions.specific_task_id import specific_task_id
from managermenus.manager_lib_menu import manager_library_menu
from managermenus.review_menu import review_menu
from classes.task_library import task_library


def manager_hub():
    while True:
        print("\n===== Welcome back to the Manager's Hub =====")
        menu_choice = input("\nHere you can:\n"
                            "1. Create a task\n"
                            "2. View all tasks in task library\n"
                            "3. View tasks pending review\n"
                            "4. Import a task\n"
                            "5. Log out\n"
                            "\nWhat action would you like to execute?\n")

        if "create" in menu_choice.lower():
            create_task()

        elif "all" in menu_choice.lower():
            task_library.print_library()
            manager_library_menu()

        elif "review" in menu_choice.lower():
            task_library.pending_review()
            yes_no = input("\nWould you like to review one of these tasks?\n")
            if "yes" in yes_no.lower():
                review_task = specific_task_id()
                review_menu(review_task)

        elif "import" in menu_choice.lower():
            import_task()

        elif "out" in menu_choice.lower():
            print("\n====== You are now logged out of the Wyeth Task"
                  " Management system =====")
            break
