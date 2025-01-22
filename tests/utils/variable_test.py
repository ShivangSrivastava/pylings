from .test_base import TestBase


class VariableTest(TestBase):
    def run(self, var_name: str, expected_value) -> str:
        self.execute_code()
        actual_value = self.namespace.get(var_name)
        if actual_value == expected_value:
            return f"Pass: Variable '{var_name}' is correctly set to {expected_value}."
        return f"Fail: Variable '{var_name}' expected {expected_value}, but got {actual_value}."
