from typing import NoReturn
from pathlib import Path

import click

@click.group()
def cmd():
    pass


@cmd.command()
@click.argument('name', type=str)
def start_project(name: str) -> NoReturn:
    repo_root: Path = Path(__file__).resolve().parents[1]

    project_root = repo_root / name
    project_root.mkdir(exist_ok=False)


if __name__ == '__main__':
    cmd()
