from taskfunctions.comment_on_task import comment_on_task
from taskfunctions.export_task import export_task
from taskfunctions.update_task import update_task
from classes.task_library import task_library


def manager_task_menu(task):
    while True:
        task.view()
        task_menu_choice = input("\n===== Task Menu =====\n"
                                 "1. Update task\n"
                                 "2. Comment on this task\n"
                                 "3. Export this task\n"
                                 "4. Delete this task\n"
                                 "5. Return to Task Library\n"
                                 "\nWhat action would you like to execute?\n")

        if "update" in task_menu_choice.lower():
            update_task(task)

        elif "comment" in task_menu_choice.lower():
            comment_on_task(task)

        elif "export" in task_menu_choice.lower():
            export_task()

        elif "delete" in task_menu_choice.lower():
            task_library.delete_task(task.unique_id)
            return

        elif "return" in task_menu_choice.lower():
            return
