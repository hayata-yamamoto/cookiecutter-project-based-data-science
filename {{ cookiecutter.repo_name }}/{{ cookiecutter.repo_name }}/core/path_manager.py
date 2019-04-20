from pathlib import Path
from typing import NoReturn, List


class PathManager:
    BASE_DIR: Path = Path(__file__).resolve().parents[1]

    def __init__(self, project: str) -> NoReturn:
        self.PROJECT_DIR: Path = self.BASE_DIR / project

        # core directory
        self.CORE = self.BASE_DIR / "core"
        self.CORE_CONFIG = self.CORE / "config"
        self.CORE_DATASETS = self.CORE / "datasets"
        self.CORE_FEATURES = self.CORE / "features"
        self.CORE_MODELS = self.CORE / "models"

        # data directory
        self.DATA_DIR: Path = self.BASE_DIR / "data" / project
        self.RAW: Path = self.DATA_DIR / "raw"
        self.INTERIM: Path = self.DATA_DIR / "interim"
        self.PROCESSED: Path = self.DATA_DIR / "processed"

        # modules directory
        self.MODULES = self.BASE_DIR / "modules"

        # tests directory
        self.TESTS = self.PROJECT_DIR / "tests" / project

        # project directory
        self.NOTEBOOKS: Path = self.PROJECT_DIR / "notebooks"
        self.EXPLORATORY: Path = self.NOTEBOOKS / "exploratory"
        self.PREDICTIVE: Path = self.NOTEBOOKS / "predictive"
        
        self.SRC: Path = self.PROJECT_DIR / "src"
        self.DATASETS: Path = self.SRC / "datasets"
        self.FEATURES: Path = self.SRC / "features"
        self.MODELS: Path = self.SRC / "models"
        self.TASKS: Path = self.SRC / "tasks"

    @staticmethod
    def mkdir_and_touch(path: Path, filename: str, parents: bool = True, exists_ok: bool = True) -> NoReturn:
        path.mkdir(parents=parents, exist_ok=exists_ok)
        (path / filename).touch()

    def get_project_data_dirs(self) -> List[Path]:
        return [self.RAW, self.INTERIM, self.PROCESSED]

    def create_project_data_dirs(self) -> NoReturn:
        map(lambda p: self.mkdir_and_touch(path=p, filename='.gitkeep'), self.get_project_data_dirs())

    def get_project_dirs(self) -> List[Path]:
        return [self.EXPLORATORY, self.PREDICTIVE, self.SRC, self.DATASETS, self.FEATURES, self.MODELS, self.TASKS]

    def create_project_dirs(self) -> NoReturn:
        map(lambda p: self.mkdir_and_touch(f, filename='__init__.py'), self.get_project_dirs())

    def get_project_test_dirs(self) -> List[Path]:
        return [self.TESTS]

    def create_project_test_dirs(self) -> NoReturn:
        map(lambda p: self.mkdir_and_touch(path=p, filename='__init__.py'), self.get_project_test_dirs())

    def create_project(self) -> NoReturn:
        self.create_project_data_dirs()
        self.create_project_dirs()
        self.create_project_test_dirs()


