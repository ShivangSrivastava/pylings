from .db_manager import DBManager


class Solution:
    def __init__(
        self,
        exercise_id: str,
        solution: str,
        hints: str | None = None,
    ):
        self.exercise_id = exercise_id
        self.solution = solution
        self.hints = hints

    @classmethod
    def from_tuple(cls, args):
        if len(args) != 3:
            raise ValueError(f"args must be of len 3, got {len(args)}")
        return cls(args[0], args[1], list(args[2]))

    def __repr__(self):
        return f"Solution({self.exercise_id})"


class SolutionManager(DBManager):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS solutions
            (exercise_id TEXT PRIMARY KEY,
            solution TEXT NOT NULL,
            hints TEXT
            )"""
        )
        self.conn.commit()

    def insert_solution(self, solution: Solution):
        self.cursor.execute(
            """
            INSERT INTO solutions (exercise_id, solution, hints)
            VALUES (?, ?, ?)""",
            (
                solution.exercise_id,
                solution.solution,
                str(solution.hints),
            ),
        )
        self.conn.commit()

    def get_solutions(self) -> list[Solution]:
        self.cursor.execute(
            "SELECT * FROM solutions",
        )
        return [Solution.from_tuple(row) for row in self.cursor.fetchall()]

    def count_total(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM solutions")
        return self.cursor.fetchone()[0]
