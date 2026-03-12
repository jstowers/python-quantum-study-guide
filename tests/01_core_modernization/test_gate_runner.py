import re
import pytest

from gate_runner import run_gate

def test_run_gate_returns_correct_number_of_results():
    results = run_gate(0, "X", [0.0], 3)
    assert len(results) == 3

def test_run_gate_returns_empty_list_for_zero_shots():
    results = run_gate(0, "X", [0.0], 0)
    assert len(results) == 0

@pytest.mark.parametrize('shots', [0, 1, 10, 100, 1000, 5000])
def test_run_gate_result_count_matches_shots(shots):
    results = run_gate(0, "X", [0.0], shots)
    assert len(results) == shots

def test_run_gate_raises_value_error_for_negative_qubit_index():
    with pytest.raises(ValueError, match=re.escape("Invalid qubit index: -1")):
        run_gate(-1, "X", [0.0], 1)

def test_run_gate_raises_type_error_for_non_integer_qubit_index():
    with pytest.raises(TypeError, match=re.escape("Qubit index must be an integer, got str")):
        run_gate("q0", "X", [0.0], 1) # type: ignore[arg-type]