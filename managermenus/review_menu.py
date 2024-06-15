from taskfunctions.comment_on_task import comment_on_task


def review_menu(task):

    while True:
        task.view()

        review_menu_choice = input("\n===== Review Menu =====\n"
                                   "1. Comment on this task\n"
                                   "2. Mark this task incomplete\n"
                                   "3. Mark this task complete\n"
                                   "4. Return to the Manager's Hub\n"
                                   "\nWhat action would you like to"
                                   " execute?\n")

        if "comment" in review_menu_choice.lower():
            comment_on_task(task)

        elif "incomplete" in review_menu_choice.lower():
            task.mark_incomplete()

        elif "complete" in review_menu_choice.lower():
            task.mark_complete()

        elif "return" in review_menu_choice.lower():
            return
