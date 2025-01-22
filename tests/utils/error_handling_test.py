from .test_base import TestBase


class ErrorHandlingTest(TestBase):
    def run(self, expected_error: str) -> str:
        try:
            exec(self.user_code)
            return f"Fail: Expected {expected_error}, but no error occurred."
        except Exception as e:
            if expected_error in str(e):
                return f"Pass: Correctly raised {expected_error}."
            return f"Fail: Expected {expected_error}, but got {str(e)}."
