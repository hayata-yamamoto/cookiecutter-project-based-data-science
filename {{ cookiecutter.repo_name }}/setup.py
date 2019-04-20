from setuptools import find_packages, setup
from pathlib import Path
from typing import IO


def main():
    f: IO
    with Path("requirements.txt").open(mode='r') as f:
        req = f.read().splitlines()

    setup(
        name='{{ cookiecutter.repo_name }}',
        packages=find_packages(exclude=["{{ cookiecutter.repo_name}}/data"]),
        install_requires=req,
        version='0.1.0',
        description='{{ cookiecutter.description }}',
    )

if __name__ == '__main__':
    main()
