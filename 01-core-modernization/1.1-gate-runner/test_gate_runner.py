import pytest

from gate_runner import run_gate

def test_run_gate_returns_correct_number_of_results():
    results = run_gate(0, "X", [0.0], 3)
    assert len(results) == 3