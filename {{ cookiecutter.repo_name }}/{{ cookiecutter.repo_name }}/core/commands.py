from typing import NoReturn

import click

from .path_manager import PathManager


@click.group()
def cmd():
    pass


@cmd.command()
@click.argument('name', type=str)
def start_project(name: str) -> NoReturn:
    manager = PathManager(project=name)




if __name__ == '__main__':
    cmd()
