"""
Pytest configuration. Adds exercise code to the import path.

This allows the tests to import the exercise code from the exercises/ folder.

Updated: Wednesday, March 11, 2026
"""
import sys
from pathlib import Path

# Project root path
root = Path(__file__).resolve().parent

# Folders containing exercise modules to be tested
sys.path.insert(0, str(root / "exercises" / "01_core_modernization"))