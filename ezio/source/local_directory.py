import os

from ..config import EzioConfig
from ..exception import SpecifiedPathDoesNotExistError
from ..type import TableLike
from .base import DataSource


class LocalDirectoryDataSource(DataSource):
    """A data source implementation for local directory.

    This class provides methods to load and save tables from/to local files.
    """

    def __init__(self, dir_path: str):
        self._path = dir_path

    @property
    def path(self) -> str:
        """str: The path to the directory."""
        return self._path

    @path.setter
    def path(self, new_path: str):
        if not os.path.exists(new_path):
            raise SpecifiedPathDoesNotExistError(new_path)

        self._path = new_path

    def load_table(self, table_data: dict, **kwargs) -> TableLike:
        engine = EzioConfig.get_engine()
        table_data["path"] = os.path.join(self.path, table_data["path"])
        table = engine.load_table_from_file(table_data, **kwargs)

        return table

    def save_table(self, table: TableLike, table_data: dict, **kwargs):
        engine = EzioConfig.get_engine()
        engine.save_table_as_file(table, table_data, **kwargs)
