import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))

from log_in import log_in


# ========== TESTING LOG-IN MODULE ==========


class TestLogIn(unittest.TestCase):

    def test_manager_no_errors(self):
        """
        Aim:
        Test the create_task function can handle anticipated user input.

        Outcome:
        No issues.
        """
        # Arrange
        with patch("builtins.input",
                   side_effect=["Manager", "12345"]):

            # Act
            details = log_in()

            # Assert
            self.assertEqual(details[0], "manager")
            self.assertEqual(details[1], "12345")

    def test_employee_no_errors(self):
        """
        Aim:
        Test the create_task function can handle anticipated user input.

        Outcome:
        No issues.
        """
        # Arrange
        with patch("builtins.input",
                   side_effect=["employee", "12345"]):

            # Act
            details = log_in()

            # Assert
            self.assertEqual(details[0], "employee")
            self.assertEqual(details[1], "12345")

    def test_three_attempts_invalid_role_input(self):
        """
        Aim:
        Test the create_task function can handle anticipated user input.

        Outcome:
        No issues.
        """
        # Arrange
        with patch("builtins.input",
                   side_effect=["it's me", "janitor", "", "employee",
                                "12345"]):

            # Act
            details = log_in()

            # Assert
            self.assertEqual(details[0], "employee")
            self.assertEqual(details[1], "12345")


if __name__ == "__main__":
    unittest.main()
