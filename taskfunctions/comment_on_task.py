def comment_on_task(task):
    from user_interface import details

    print("\n===== Comment on Task =====\n")
    yes_no = input("Are you sure you would like to comment on this"
                   " task?\n")

    if "yes" in yes_no.lower():
        contents = input("Please enter your comment: \n")
        author_id = details[1]

        task.add_comment(contents, author_id)
