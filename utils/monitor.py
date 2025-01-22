"""
run to clear previous screen : done

current running program and error


seperator ------------
- help goes here

[###-----------------]
percentage completed 34%


key map
q:quit     h:help


"""

import os
import platform

import typer


class Monitor:
    @staticmethod
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def seperator():
        return "\n"

    @staticmethod
    def progress_bar(completed, total):
        percent = int(100 * (completed / total))
        hash_count = percent // 5
        return f"[{'#' * hash_count}{'=' * (20 - hash_count)}]\n{percent}% completed"

    @staticmethod
    def keymap():
        return "Keymap: q: quit      h: hints      r: refresh"

    @staticmethod
    def hints(hint):
        return f"Hints:\n{hint}"

    def show(self, content, hint, completed, total):
        self.clear_screen()
        typer.echo(self.seperator())
        typer.echo(content)
        typer.echo(self.seperator())
        typer.echo(self.hints(hint))
        typer.echo(self.seperator())
        typer.echo(self.progress_bar(completed, total))
        typer.echo(self.seperator())
        typer.echo(self.keymap())
