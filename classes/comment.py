class Comment:
    def __init__(self, contents, author_id, timestamp) -> None:
        self.contents = contents
        self.author_id = author_id
        self.timestamp = timestamp

    def __str__(self):
        return (f"Staff ID {self.author_id} commented:\n"
                f"{self.contents}\n"
                f"Time comment left: {self.timestamp}\n"
                )
