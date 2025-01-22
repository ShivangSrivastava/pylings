from .test_base import TestBase


class OutputTest(TestBase):
    def run(self, expected_output: str) -> str:
        self.execute_code()
        if self.output == expected_output:
            return "Pass: Output matches expected output."
        return f"Fail: Expected '{expected_output}', but got '{self.output}'"
