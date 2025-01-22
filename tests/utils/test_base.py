import io
import sys


class TestBase:
    def __init__(self, user_code: str):
        self.user_code = user_code
        self.namespace = {}
        self.output = None

    def execute_code(self):
        """Executes the user's code and captures its namespace and output."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            exec(self.user_code, {}, self.namespace)
            self.output = captured_output.getvalue().strip()
        except Exception as e:
            self.output = f"Error: {e}"
        finally:
            sys.stdout = sys.__stdout__
