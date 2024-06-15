from classes.task_library import random_task_generation


def import_task():
    print("\n=== Import Task(s) ===\n")
    yes_no = input("Are you sure you would like to import a task from an"
                   " external system?\n")
    if "yes" in yes_no.lower():
        num_import = input("\nHow many tasks would you like to import?\n")
        random_task_generation(int(num_import))
        if int(num_import) > 1:
            print("\nTasks successfully imported!\n")
        else:
            print("\nTask successfully imported!\n")
    else:
        return
