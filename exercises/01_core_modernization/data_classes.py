"""
1.2: Refactor Config Dict to DataClass

Reference:  Study Guide, section 1.2, page 14
Updated:    Thursday, March 12, 2026

Problem:

Convert this fragile dictionary into a safe, typed @dataclass.

pulse_config = {
    'frequency_hz': 5.1e9
    'amplitude': 0.85,
    'duration_ns': 40,
    'backend': 'ibm_kyoto',
    'tags': ['calibration', 'q0']
}
"""

from dataclasses import dataclass, field

@dataclass
class Config:
    frequency_hz: float
    amplitude: float
    duration_ns: int
    backend: str
    tags: list[str] = field(default_factory=list)

def run_gate(config: Config) -> None:
    print(f"Running gate with config: {config}")