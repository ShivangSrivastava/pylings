import os

PROJECT_PATH = os.getcwd()
EXERCISE_PATH = os.path.join(PROJECT_PATH, "exercises")
TEST_PATH = os.path.join(PROJECT_PATH, "tests")
SOLUTION_PATH = os.path.join(PROJECT_PATH, "solutions")
DB_PATH = os.path.join(PROJECT_PATH, "pylings.db")

PREDEFINED_ORDER = [
    "basics",
    "loops",
]
