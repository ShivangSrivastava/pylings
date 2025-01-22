from pathlib import Path

import typer

from utils import constants


class LSCommand:
    @staticmethod
    def execute():
        for p in Path(constants.EXERCISE_PATH).rglob("*"):
            if p.is_dir():
                typer.echo(
                    f"{p.name}: {p.relative_to(constants.PROJECT_PATH)}"
                )
