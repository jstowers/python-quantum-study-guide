"""
1.1 Add type hints to a legacy gate runner

Problem: 
The `run_gate` function below is untyped:

def run_gate(qubit, gate_name, angles, shots):
    results = []

    for i in range(shots):
        r = execute(qubit, gate_name, angles)
        results.append(r)

    return results

Add complete annotations and a docstring.
Use Sequence, np.ndarray, and a TypeAlias for QubitId.

"""

from typing import Sequence, TypeAlias
import random
import numpy as np

QubitId: TypeAlias = int

"""
Sequence[float] is a broader type than `list[]`.  It accepts any
ordered, indexable collection: list, tuple, NumPy array, etc.

In quantum software, angles often come from NumPy as arrays, or 
from other functions as tuples.
"""

def run_gate(qubit: QubitId, gate_name: str, angles: Sequence[float], shots: int) -> list[np.ndarray]:
    """ 
    Run a quantum gate on a qubit a given number of times and return measurement results.

    Args:
        qubit:      index of the target qubit
        gate_name:  name of the gate to apply, e.g. "X", "RZ"
        angles:     rotation angles in radians
        shots:      number of times to repeat the measurement

    Returns:
        a list of measurement results, one per shot
    """
    if not isinstance(qubit, int):
        raise TypeError(f"Qubit index must be an integer, got {type(qubit).__name__}")
    if qubit < 0:
        raise ValueError(f"Invalid qubit index: {qubit} (must be >= 0)")

    results: list[np.ndarray] = []

    for i in range(shots):
        r = execute(qubit, gate_name, angles)
        results.append(r)

    return results

## stub execute function
def execute(qubit: QubitId, gate_name: str, angles: Sequence[float]) -> np.ndarray:
    # stub simulating a hardware gate execution result
    return np.random.randint(0, 2, size=1).astype(float)