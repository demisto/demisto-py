import unittest


class TestUpdateAutomationExample(unittest.TestCase):
    EXAMPLE_PATH = './examples/update_automation_example.py'

    def test_run_example(self):
        """
        Given: A demisto instance.
        When: Running the update_automation_example.py script.
        Then: Ensure no errors are raised.
        """
        with open(self.EXAMPLE_PATH) as example_file:
            exec(example_file.read())
