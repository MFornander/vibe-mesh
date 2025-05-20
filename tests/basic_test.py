from pathlib import Path


def test_something() -> None:
    assert Path(__file__).is_file()
