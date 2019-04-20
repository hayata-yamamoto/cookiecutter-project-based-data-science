from pathlib import Path
from typing import NoReturn


class PathManager:
    BASE_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_ROOT: Path = BASE_DIR / "data"

    def __init__(self, project: str) -> NoReturn:
        self.project = project
        self.PROJECT_ROOT: Path = self.BASE_DIR / self.project
        self.PROJECT_DATA_ROOT: Path = self.DATA_ROOT / self.project

        # core directory
        self.CORE_ROOT = self.PROJECT_ROOT / "core"

        # data directory
        self.RAW_DIR: Path = self.PROJECT_DATA_ROOT / "raw"
        self.INTERIM_DIR: Path = self.PROJECT_DATA_ROOT / "interim"
        self.PROCESSED_DIR: Path = self.PROJECT_DATA_ROOT / "processed"

        # src directory
        self.NOTEBOOK_DIR = self.PROJECT_ROOT / "notebooks"
        self.SRC_ROOT = self.PROJECT_ROOT / "src"
        self.DATASETS_DIR = self.SRC_ROOT / "datasets"
        self.FEATURES_DIR = self.SRC_ROOT / "features"
        self.MODELS_DIR = self.SRC_ROOT / "models"
        self.TASKS_DIR = self.SRC_ROOT / "tasks"
        self.TESTS_DIR = self.SRC_ROOT / "tests"

    def get_project_data_dirs(self):
        return [self.RAW_DIR, self.INTERIM_DIR, self.PROCESSED_DIR]

    def get_project_dirs(self):
        return [self.NOTEBOOK_DIR, self.SRC_ROOT, self.DATASETS_DIR, self.FEATURES_DIR,
                self.MODELS_DIR, self.TASKS_DIR, self.TESTS_DIR]

    def create_project(self):
        dirs = self.get_project_data_dirs()
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
            (d / ".gitkeep").touch()

        dirs = self.get_project_dirs()
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
            (d / "__init__.py").touch()

