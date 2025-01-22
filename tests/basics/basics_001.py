"""
Tests for Exercise 1: Variable Declaration

Purpose:
These tests check the correctness of the variable assignments. Specifically, they verify:
- The value of `message` is correctly set to "Hello, pylings!".
- The value of `x` is correctly set to 20.
No edge cases or input-output validations are required for this exercise.
"""

import os

from tests.utils.variable_test import VariableTest
from utils import constants


def test_basics():
    with open(
        os.path.join(constants.EXERCISE_PATH, "basics", "basics_001.py")
    ) as f:
        content = f.read()

    vt = VariableTest(content)
    return vt.run("x", 20)
