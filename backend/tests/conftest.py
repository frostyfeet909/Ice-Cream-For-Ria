"""Configuration for pytest.

Loads the test environment for pytest.

Provides:
-
"""

from pathlib import Path

from dotenv import load_dotenv

DIR__test_data = Path("api", "tests", "data")  # type: ignore - Loading the test envionrment
res = load_dotenv(DIR__test_data / "test.env", override=True)  # type: ignore - Loading the test envionrment
print("Loaded test.env:", res)  # type: ignore - Loading the test envionrment
