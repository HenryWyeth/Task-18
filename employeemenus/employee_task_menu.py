from taskfunctions.comment_on_task import comment_on_task


def employee_task_menu(task):
    while True:
        task.view()

        task_menu_choice = input("\n===== Task Menu =====\n"
                                 "1. Comment on this task\n"
                                 "2. Submit this task for review\n"
                                 "3. Return to Employee Hub\n"
                                 "\nWhat action would you like to execute?\n")

        if "comment" in task_menu_choice.lower():
            comment_on_task(task)

        elif "submit" in task_menu_choice.lower():
            task.submit_for_review()

        elif "return" in task_menu_choice.lower():
            return
