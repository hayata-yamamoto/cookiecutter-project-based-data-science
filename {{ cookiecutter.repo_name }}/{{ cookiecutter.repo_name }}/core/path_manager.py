from pathlib import Path
from typing import NoReturn, List


class PathManager:
    BASE_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_DIR: Path = BASE_DIR / "data"
    CORE: Path = BASE_DIR / "core"
    CORE_CONFIG: Path = CORE / "config"
    CORE_DATASETS: Path = CORE / "datasets"
    CORE_FEATURES: Path = CORE / "features"
    CORE_MODELS: Path = CORE / "models"
    MODULES: Path = BASE_DIR / "modules"
    TESTS: Path = BASE_DIR / "tests"

    def __init__(self, project: str) -> NoReturn:
        self.PROJECT_DIR: Path = self.BASE_DIR / project
        self.PROJECT_TEST_DIR = self.TESTS / project
        self.PROJECT_DATA_DIR: Path = self.DATA_DIR / project

        # data directory
        self.RAW: Path = self.PROJECT_DATA_DIR / "raw"
        self.INTERIM: Path = self.PROJECT_DATA_DIR / "interim"
        self.PROCESSED: Path = self.PROJECT_DATA_DIR / "processed"

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


