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
    duration_ns: int = 20
    backend: str = 'ibm_kyoto'
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not 0.0 <= self.amplitude <= 1.0:
            raise ValueError(f"amplitude must be between 0.0 and 1.0, got {self.amplitude}")
        if self.duration_ns <= 0:
            raise ValueError(f"duration_ns must be positive, got {self.duration_ns}")

def run_gate(config: Config) -> None:
    print(f"Running gate with config: {config}")

## only run this code if the file is executed directly,
## not if it is imported as a module
if __name__ == "__main__":
    config = Config(
        frequency_hz = 5.1e9,
        amplitude = 0.85,
        duration_ns = 20,
        backend = "ibm_kyoto",
        tags = ["calibration", "q0"],
    )
    run_gate(config)