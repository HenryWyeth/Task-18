def log_in():
    """
    Acting as log-in screen to access the task management program.
    Currently has limited scope (no log-in failure message or password request)
    as no established users yet.

    Returns:
    role: Staff job role, influences the level of access to system features.
    staff_id: Unique to the member of staff, used as part of their activity
    documentation.
    """

    while True:
        role = input("\n=== Welcome to the Wyeth Task Management System! ===\n"
                     "Are you logging in as a Manager or Employee? \n")
        if role.lower() == "manager" or role.lower() == "employee":
            staff_id = input("\nPlease enter your staff ID number: \n")
            return role.lower(), staff_id
