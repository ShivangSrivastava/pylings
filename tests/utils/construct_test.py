import ast

from .test_base import TestBase


class ConstructTest(TestBase):
    def run(self, construct_type: str) -> str:
        try:
            tree = ast.parse(self.user_code)
            for node in ast.walk(tree):
                if construct_type == "loop" and isinstance(
                    node, (ast.For, ast.While)
                ):
                    return "Pass: Loop construct found."
                if construct_type == "function" and isinstance(
                    node, ast.FunctionDef
                ):
                    return "Pass: Function construct found."
            return f"Fail: {construct_type.capitalize()} construct not found."
        except Exception as e:
            return f"Error during construct check: {e}"
