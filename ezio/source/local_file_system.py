from ..config import EzioConfig
from ..type import TableLike
from .base import DataSource


class LocalFileSystemDataSource(DataSource):
    """A data source implementation for local file system storage.

    This class provides methods to load and save tables from/to local files.
    """

    def load_table(self, table_data: dict, **kwargs) -> TableLike:
        engine = EzioConfig.get_engine()
        table = engine.load_table_from_file(table_data, **kwargs)

        return table

    def save_table(self, table: TableLike, table_data: dict, **kwargs):
        engine = EzioConfig.get_engine()
        engine.save_table_as_file(table, table_data, **kwargs)
