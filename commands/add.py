import os
import re
from pathlib import Path

from utils import constants
from utils.template import Template


class AddCommand:
    def __init__(self, chapter: str | None):
        self.chapter = chapter
        self.file_name = None

    def create_files(self):
        self.__get_file_name()

        # Paths and contents
        paths_and_contents = [
            (constants.EXERCISE_PATH, Template().exercise()),
            (constants.SOLUTION_PATH, Template().solution()),
            (constants.TEST_PATH, Template().test()),
        ]

        # Create and write files using the helper method
        for path, content in paths_and_contents:
            self.__create_and_write_file(
                os.path.join(path, self.chapter), content
            )

    def __create_and_write_file(self, path, content):
        """Helper method to create file and write content."""
        # Ensure the directory exists
        os.makedirs(path, exist_ok=True)

        # Write content to the file
        with open(os.path.join(path, self.file_name), "w") as f:
            f.write(content)

    def __get_file_name(self):
        chapter_dir = Path(constants.EXERCISE_PATH) / self.chapter

        if chapter_dir.is_dir():
            files = list(chapter_dir.iterdir())

            chapter_files = [
                f.name
                for f in files
                if re.match(rf"^{self.chapter}_\d{{3}}\.py$", f.name)
            ]

            if not chapter_files:
                self.file_name = f"{self.chapter}_001.py"
                return

            highest_number = max(
                int(re.search(r"(\d{3})", f).group()) for f in chapter_files
            )
            next_number = highest_number + 1

            self.file_name = f"{self.chapter}_{next_number:03}.py"

        else:
            self.file_name = f"{self.chapter}_001.py"
