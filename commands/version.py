import toml
import typer


def get_version(file_path="pyproject.toml"):
    data = toml.load(file_path)
    return data["project"]["version"]


def get_name(file_path="pyproject.toml"):
    data = toml.load(file_path)
    return data["project"]["name"]


def version_callback(value: bool):
    if value:
        typer.echo(f"{get_name()}: {get_version()}")
        raise typer.Exit()
