from classes.task_library import task_library


def delete_task(task):
    task_library.delete_task(task.unique_id)
