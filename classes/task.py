from classes.comment import Comment
from datetime import datetime


class Task:
    def __init__(self,
                 unique_id,
                 title,
                 priority,
                 due_date,
                 status) -> None:
        self.unique_id = unique_id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.comments = []

    def view(self):
        print(f"Unique ID: {self.unique_id}\n")
        print(f"Task Title: {self.title}\n")
        print(f"Priority: {self.priority}\n")
        print(f"Due Date: {self.due_date}\n")
        print(f"Status: {self.status}\n")
        print("Comments:")
        for idx, comment in enumerate(self.comments, start=1):
            print(f"{idx} - {comment}")

    def update_task(self, attribute, new_value):
        if hasattr(self, attribute):
            setattr(self, attribute, new_value)
            print(f"{attribute} successfully updated to {new_value}.")
        else:
            print((f"Task has no attribute '{attribute}'."))

    def add_comment(self, contents, author_id):
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        comment = Comment(contents, author_id, timestamp)
        self.comments.append(comment)
        print("\nComment successfully added to the task.\n")

    def mark_incomplete(self):
        self.status = "Incomplete"

    def submit_for_review(self):
        self.status = "Submitted for Review"

    def mark_complete(self):
        self.status = "Complete"
