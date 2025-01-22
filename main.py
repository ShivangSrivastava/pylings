import typer

import commands
from utils import constants

app = typer.Typer(
    help="Pylings: CLI tool for practicing Python.",
    invoke_without_command=True,
)


@app.callback()
def main(
    ctx: typer.Context,
    _version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=commands.version_callback,
        is_eager=True,
        help="Show the version of the application and exit.",
    ),
):
    if not ctx.invoked_subcommand:
        commands.StartCommand()


@app.command(help="Add a new exercise template.", no_args_is_help=True)
def add(
    chapter: str = typer.Option(
        "--chapter",
        "-c",
        help="Specify an existing chapter or add a new one.",
    ),
):
    if chapter:
        commands.AddCommand(chapter).create_files()


@app.command(
    help=(
        "Initialize the application, setting up necessary directories and databases."
    )
)
def init():
    commands.InitCommand(
        exercise_path=constants.EXERCISE_PATH,
        solution_path=constants.SOLUTION_PATH,
        predefined_order=constants.PREDEFINED_ORDER,
    ).execute()


@app.command(help="List all available chapters.")
def ls():
    commands.LSCommand().execute()


@app.command(help="Clean up temporary files or reset progress.")
def reset():
    pass


if __name__ == "__main__":
    app()
