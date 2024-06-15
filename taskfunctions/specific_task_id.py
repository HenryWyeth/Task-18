from classes.task_library import task_library


def specific_task_id():
    print("\n=== View Specific Task ===\n")
    while True:
        unique_id = input("Please enter the Unique ID of the task you"
                          " wish to view: \n")
        if "return" in unique_id.lower():
            return
        task = task_library.get_task(unique_id)
        if task:
            return task
        else:
            print("\nNo task found in library with the Unique ID:"
                  f" {unique_id}.\n To return to the previous menu"
                  " please enter 'return'.")
