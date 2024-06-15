import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))

from classes.task_library import task_library
from taskfunctions.create_task import create_task


# ========== TESTING CREATE TASK MODULE ==========


class TestCreateTask(unittest.TestCase):

    def test_no_errors(self):
        """
        Aim:
        Test the create_task function can handle anticipated user input.

        Outcome:
        No issues.
        """
        # Arrange
        with patch("builtins.input",
                   side_effect=["New Title", "Low", "2024/05/22",
                                "Incomplete"]) as _:
            task_library.task_library.clear()

            # Act
            create_task()

            # Assert
            last_added_task = list(task_library.task_library.values())[-1]
            self.assertEqual(last_added_task.title, "New Title")
            self.assertEqual(last_added_task.priority, "Low")
            self.assertEqual(last_added_task.due_date, "2024/05/22")
            self.assertEqual(last_added_task.status, "Incomplete")

    def test_three_attempts_no_title_input(self):
        """
        Aim:
        Test the create_task function can handle no title input.

        Outcome:
        Initially, the function accepted no input ("") as a valid title input
        so the function was modified to show an error message and repeat the
        request for input until valid input is provided.
        """

        # Arrange
        with patch("builtins.input",
                   side_effect=["", "", "", "New Title", "Low", "2024/05/22",
                                "Incomplete"]):
            task_library.task_library.clear()

            # Act
            create_task()

            # Assert
            last_added_task = list(task_library.task_library.values())[-1]
            self.assertEqual(last_added_task.title, "New Title")
            self.assertEqual(last_added_task.priority, "Low")
            self.assertEqual(last_added_task.due_date, "2024/05/22")
            self.assertEqual(last_added_task.status, "Incomplete")

    def test_three_attempts_invalid_priority_input(self):
        """
        Aim:
        Test the create_task function can handle three incorrect priority
        inputs.

        Outcome:
        No issues.
        """

        # Arrange
        with patch("builtins.input",
                   side_effect=["New Title", "Urgent", "Small",
                                "", "Low", "2024/05/22",
                                "Incomplete"]):
            task_library.task_library.clear()

            # Act
            create_task()

            # Assert
            last_added_task = list(task_library.task_library.values())[-1]
            self.assertEqual(last_added_task.title, "New Title")
            self.assertEqual(last_added_task.priority, "Low")
            self.assertEqual(last_added_task.due_date, "2024/05/22")
            self.assertEqual(last_added_task.status, "Incomplete")

    def test_three_attempts_invalid_due_date_input(self):
        """
        Aim:
        Test the create_task function can handle three incorrect due_date
        inputs.

        Outcome:
        No issues.
        """

        # Arrange
        with patch("builtins.input",
                   side_effect=["New Title", "Medium", "ASAP",
                                "25/12/24", "", "2024/05/22",
                                "Incomplete"]):
            task_library.task_library.clear()

            # Act
            create_task()

            # Assert
            last_added_task = list(task_library.task_library.values())[-1]
            self.assertEqual(last_added_task.title, "New Title")
            self.assertEqual(last_added_task.priority, "Medium")
            self.assertEqual(last_added_task.due_date, "2024/05/22")
            self.assertEqual(last_added_task.status, "Incomplete")

    def test_three_attempts_invalid_status_input(self):
        """
        Aim:
        Test the create_task function can handle three incorrect status
        inputs.

        Outcome:
        No issues.
        """

        # Arrange
        with patch("builtins.input",
                   side_effect=["New Title", "Low", "2024/05/22",
                                "Not Done Yet", "Competed", "",
                                "Incomplete"]):
            task_library.task_library.clear()

            # Act
            create_task()

            # Assert
            last_added_task = list(task_library.task_library.values())[-1]
            self.assertEqual(last_added_task.title, "New Title")
            self.assertEqual(last_added_task.priority, "Low")
            self.assertEqual(last_added_task.due_date, "2024/05/22")
            self.assertEqual(last_added_task.status, "Incomplete")


if __name__ == "__main__":
    unittest.main()
