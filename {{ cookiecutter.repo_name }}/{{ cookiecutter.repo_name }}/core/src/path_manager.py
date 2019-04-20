from dataclasses import dataclass
from pathlib import Path


@dataclass
class PathManager:
    project_name: str
    BASE_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_ROOT: Path = BASE_DIR / "data"
    PROJECT_ROOT: Path = BASE_DIR / project_name
    RAW_DIR = PROJECT_ROOT / "raw"
    INTERIM_DIR = PROJECT_ROOT / "interim"
    PROCESSED_DIR = PROJECT_ROOT / "processed"


