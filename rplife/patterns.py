from dataclasses import dataclass
import tomllib
from pathlib import Path
from copy import deepcopy

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )


def get_pattern(name: str, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])


def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [Pattern.from_toml(name, toml_data) for name, toml_data in data.items()]


def generate_pattern(text: str):
    """Generate Conway patterns based on a string"""
    sequence = set()

    for char in text:
        char = str(ord(char))
        x = int(char[0])
        y = int(char[1:][0])
        sequence.add((x, y))
        sequence.add((x + 1, y))

    return Pattern(name=text, alive_cells=sequence)
