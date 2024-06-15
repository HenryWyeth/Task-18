from log_in import log_in
from classes.task_library import random_task_generation
from managermenus.manager_hub import manager_hub
from employeemenus.employee_hub import employee_hub


def start_application():

    global details
    details = log_in()

    random_task_generation(10)

    if details[0] == "manager":
        manager_hub()

    elif details[0] == "employee":
        employee_hub()
