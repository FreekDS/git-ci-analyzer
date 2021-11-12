from analyzer.Repository.Repo import Repo
from typing import List


class TestRepo(Repo):
    def __init__(self, path, existing_paths: List[str] = None, empty_dirs: List[str] = None, repo_type='test'):
        existing_paths = [] if existing_paths is None else existing_paths
        empty_dirs = [] if empty_dirs is None else empty_dirs
        super().__init__(path, repo_type)
        self.existing_paths = existing_paths + empty_dirs
        self.empty_dirs = empty_dirs

    def path_exists(self, path) -> bool:
        return path in self.existing_paths

    def dir_empty(self, path):
        return path in self.empty_dirs

    def fetch_builtin_ci(self):
        """does nothing"""
