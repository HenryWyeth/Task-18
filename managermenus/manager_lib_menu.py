from taskfunctions.create_task import create_task
from taskfunctions.export_task import export_task
from taskfunctions.import_task import import_task
from taskfunctions.specific_task_id import specific_task_id
from managermenus.manager_task_menu import manager_task_menu
from classes.task_library import task_library


def manager_library_menu():
    while True:
        lib_menu_choice = input("\n===== Task Library Menu =====\n"
                                "1. Display current library\n"
                                "2. Create a new task\n"
                                "3. Import a task\n"
                                "4. View an individual task\n"
                                "5. Sort tasks by category\n"
                                "6. Search tasks by keyword\n"
                                "7. Delete a task\n"
                                "8. Export a task\n"
                                "9. Return to Manager's Hub\n"
                                "\nWhat action would you like to execute?\n")

        if "display" in lib_menu_choice.lower():
            task_library.print_library()

        elif "create" in lib_menu_choice.lower():
            create_task()

        elif "import" in lib_menu_choice.lower():
            import_task()

        elif "view" in lib_menu_choice.lower():
            view_task = specific_task_id()
            manager_task_menu(view_task)

        elif "sort" in lib_menu_choice.lower():
            print("\n=== Sort Tasks ===\n")
            category_choice = input("By which category do you wish to sort"
                                    " the task library?\n ('Title',"
                                    " 'Priority', 'Due Date', or 'Status')\n")
            task_library.sort_tasks(category_choice)

        elif "search" in lib_menu_choice.lower():
            print("\n=== Search for Tasks===\n")
            keyword = input("Please enter the keyword you wish to search:\n")
            task_library.search_tasks(keyword)

        elif "delete" in lib_menu_choice.lower():
            print("\n=== Delete Task ===\n")
            del_unique_id = input("Please enter the Unique ID of the task you"
                                  " wish to delete: \n")
            task_library.delete_task(del_unique_id)

        elif "export" in lib_menu_choice.lower():
            print("\n=== Export Task ===\n")
            export_unique_id = input("Please enter the Unique ID of the task"
                                     "you wish to export: \n")
            if export_unique_id not in task_library.task_library:
                print("No task found in library with the Unique ID:"
                      f" {export_unique_id}")
            else:
                export_task()

        elif "return" in lib_menu_choice.lower():
            return
