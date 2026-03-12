# Core Modernization

## Topics

### 1.1 Type hints and annotations

`Sequence[float]` is a broader type than `list[]`.  It accepts any ordered, indexable collection: list, tuple, NumPy array, etc.

In quantum software, angles often come from NumPy as arrays, or from other functions as tuples.

### 1.2 Data classes and structured configuration

### 1.3 Pathlib - modern file paths

### 1.4 Context managers

## Unit Tests

I use `pytest` for unit tests.

To run a specific unit test, go to the folder for that exercise and specify the test file and verbose `-v` output

```bash
pytest test_gate_runner.py -v
```

## Test Passes

If the test passes, you will see output like:

![test-success-sample](./image/test-success-sample.png)


### Test Fails

If the test fails, you will see output like:

![test-failure-sample](./image/test-failure-sample.png)


## First Commit

Tuesday, March 10, 2026

## Last Revision

Wednesday, March 11, 2026