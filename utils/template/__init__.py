import os


class Template:
    def __init__(self, template_dir="utils/template"):
        # Initialize with the directory where templates are stored
        self.template_dir = template_dir

    def _read_template(self, template_name):
        """Helper function to read template files."""
        template_path = os.path.join(self.template_dir, f"{template_name}.py")
        with open(template_path) as f:
            return f.read()

    def exercise(self):
        return self._read_template("exercise_template")

    def solution(self):
        return self._read_template("solution_template")

    def test(self):
        return self._read_template("test_template")
