import os
import re

import typer

from utils import constants, db

from .reset import ResetCommand


class InitCommand:
    def __init__(self, exercise_path, solution_path, predefined_order):
        self.exercise_path = exercise_path
        self.solution_path = solution_path
        self.predefined_order = predefined_order
        self._check_already_initiated()

    @staticmethod
    def _check_already_initiated():
        if os.path.exists(
            constants.DB_PATH
        ):  # Check if the database file already exists
            typer.echo(
                "pylints already initiated. Try using the reset command to reset your progress."
            )
            typer.Exit()

    def _get_files_from_directory(self, directory):
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(".py"):
                    files.append(os.path.splitext(filename)[0])
        return files

    def _get_ordered_files(self, directory):
        all_files = self._get_files_from_directory(directory)
        ordered_files = [
            file for file in self.predefined_order if file in all_files
        ]
        remaining_files = [
            file for file in all_files if file not in ordered_files
        ]
        return ordered_files + remaining_files

    def _get_solution_and_hints(self, solution_file):
        with open(solution_file, "r") as f:
            solution_content = f.read()

        hints = self._extract_hints(solution_content)

        solution_content = solution_content.split("# Hints:")[0].strip()

        return solution_content, hints

    def _extract_hints(self, solution_content):
        hints_section = re.search(
            r'# Hints:\s*"""\s*(.*?)\s*"""', solution_content, re.DOTALL
        )
        if hints_section:
            return [
                hint.strip()
                for hint in hints_section.group(1).splitlines()
                if hint.strip()
            ]
        return []

    def insert_exercise(self, exercise: db.Exercise):
        db.ExerciseManager().insert_exercise(
            db.Exercise(file_path=exercise.file_path, content=exercise.content)
        )

    def execute(self):
        for exercise_id in self._get_ordered_files(self.exercise_path):
            exercise_file_path = os.path.join(
                self.exercise_path,
                "_".join(exercise_id.split("_")[:-1]),
                f"{exercise_id}.py",
            )
            with open(exercise_file_path, "r") as f:
                exercise_content = f.read()
            exercise = db.Exercise(
                file_path=exercise_file_path, content=exercise_content
            )
            self.insert_exercise(exercise)
            db.ProgressManager().insert_progress(
                db.Progress(exercise_id=exercise_id)
            )

        for solution_id in self._get_ordered_files(self.solution_path):
            solution_file = os.path.join(
                self.solution_path,
                "_".join(exercise_id.split("_")[:-1]),
                f"{solution_id}.py",
            )
            solution_content, hints = self._get_solution_and_hints(
                solution_file
            )
            db.SolutionManager().insert_solution(
                db.Solution(
                    exercise_id=solution_id,
                    solution=solution_content,
                    hints=hints,
                )
            )
        ResetCommand.delete_all_files_in_directory(constants.SOLUTION_PATH)
