# Exercise 1.2: Refactor Config Dict to DataClass
# Study guide reference:  Section 1.2, p. 14
# Updated: Wednesday, March 11, 2026

from dataclasses import dataclass

@dataclass
class Config:
    shots: int
    qubit_index: int
    gate: str
    angle: float

def run_gate(config: Config) -> list[float]: