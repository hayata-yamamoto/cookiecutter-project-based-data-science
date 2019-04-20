from typing import NoReturn

import click

from .path_manager import PathManager


@click.group()
def cmd():
    pass


@cmd.command()
@click.argument('name', type=str)
def start_project(name: str) -> NoReturn:
    PathManager(name).create_project()
    

if __name__ == '__main__':
    cmd()
