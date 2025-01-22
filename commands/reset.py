import os
import shutil

from utils import db


class ResetCommand:
    def __init__(self, solutions_path):
        self.solutions_path = solutions_path

    @staticmethod
    def delete_all_files_in_directory(directory):
        for root, dirs, files in os.walk(directory, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))

    @staticmethod
    def update_progress_status_to_incomplete():
        progress_list = db.ProgressManager().get_progresses()
        for progress in progress_list:
            progress.status = db.Status.INCOMPLETE
            db.ProgressManager().update_progress(progress)

    def execute(self):
        self._delete_all_files_in_directory(self.solutions_path)

        self._update_progress_status_to_incomplete()
