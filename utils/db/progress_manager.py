from datetime import datetime

from .db_manager import DBManager
from .status_enum import Status


class Progress:
    def __init__(
        self,
        exercise_id: str,
        status: Status = Status.INCOMPLETE,
        last_attempt: datetime | None = None,
    ):
        self.exercise_id = exercise_id
        self.status = status
        self.last_attempt = last_attempt

    @classmethod
    def from_tuple(cls, args):
        if len(args) != 3:
            raise ValueError(f"args must be of len 3, got {len(args)}")
        return cls(
            exercise_id=args[0],
            status=Status[args[1]],
            last_attempt=(
                datetime.strptime(args[2], "%Y-%m-%d %H:%M:%S")
                if args[2]
                else None
            ),
        )

    def __repr__(self):
        return f"Progress({self.exercise_id}, {self.status.name})"


class ProgressManager(DBManager):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exercise_id TEXT,
        status TEXT,
        last_attempt TIMESTAMP
        )
        """
        )
        self.conn.commit()

    def insert_progress(self, progress: Progress):
        self.cursor.execute(
            """
        INSERT INTO progress (exercise_id, status)
        VALUES (?, ?)
        """,
            (
                progress.exercise_id,
                progress.status.name,
            ),
        )
        self.conn.commit()

    def update_progress(self, progress: Progress):
        self.cursor.execute(
            """
        UPDATE progress
        SET status = ?, last_attempt = CURRENT_TIMESTAMP
        WHERE exercise_id = ?
        """,
            (
                progress.status.name,
                progress.exercise_id,
            ),
        )
        self.conn.commit()

    def get_progresses(self) -> list[Progress]:
        self.cursor.execute(
            "SELECT * FROM progress ORDER BY id",
        )
        return [Progress.from_tuple(row) for row in self.cursor.fetchall()]

    def count_completed(self) -> int:
        self.cursor.execute(
            "SELECT COUNT(*) FROM progress WHERE status = 'COMPLETE'"
        )
        return self.cursor.fetchone()[0]

    def count_total(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM progress")
        return self.cursor.fetchone()[0]
