from dataclasses import dataclass
from pathlib import Path


@dataclass
class PathManager:
    project: str

    BASE_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_ROOT: Path = BASE_DIR / "data"
    PROJECT_ROOT: Path = BASE_DIR / project
    PROJECT_DATA_ROOT: Path = DATA_ROOT / project

    # core directory
    CORE_ROOT = PROJECT_ROOT / "core"

    # data directory
    RAW_DIR: Path = PROJECT_DATA_ROOT / "raw"
    INTERIM_DIR: Path = PROJECT_DATA_ROOT / "interim"
    PROCESSED_DIR: Path = PROJECT_DATA_ROOT / "processed"

    # src directory
    NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
    SRC_ROOT = PROJECT_ROOT / "src"
    DATASETS_DIR = SRC_ROOT / "datasets"
    FEATURES_DIR = SRC_ROOT / "features"
    MODELS_DIR = SRC_ROOT / "models"
    TASKS_DIR = SRC_ROOT / "tasks"
    TESTS_DIR = SRC_ROOT / "tests"

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

