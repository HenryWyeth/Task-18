def export_task():
    yes_no = input("\nAre you sure you want to export this task"
                   " to an external system?\n")
    if "yes" in yes_no.lower():
        print("\nTask successfully exported!\n")
