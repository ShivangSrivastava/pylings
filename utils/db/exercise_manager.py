from .db_manager import DBManager


class Exercise:
    def __init__(self, file_path: str, content: str):
        self.file_path = file_path
        self.content = content

    @classmethod
    def from_tuple(cls, args):
        if len(args) != 2:
            raise ValueError(f"args must be of len 2, got {len(args)}")
        return cls(args[0], args[1])

    def __repr__(self):
        return f"Exercise({self.file_path})"


class ExerciseManager(DBManager):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS exercises(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL,
            content TEXT NOT NULL
            )"""
        )
        self.conn.commit()

    def insert_exercise(self, exercise: Exercise):
        self.cursor.execute(
            """
            INSERT INTO exercises (file_path, content)
            VALUES (?, ?)""",
            (exercise.file_path, exercise.content),
        )
        self.conn.commit()

    def get_exercises(self) -> list[Exercise]:
        self.cursor.execute(
            "SELECT * FROM exercises",
        )
        return [Exercise.from_tuple(row) for row in self.cursor.fetchall()]
