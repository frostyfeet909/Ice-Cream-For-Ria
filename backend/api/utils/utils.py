import tomllib
from pathlib import Path


def get_version() -> str:
    """Get version information from poetry."""
    poetry_project_file = Path(__file__).parent.parent.parent / "pyproject.toml"
    with poetry_project_file.open(mode="rb") as f:
        poetry_project = tomllib.load(f)

    return poetry_project["tool"]["poetry"]["version"]
