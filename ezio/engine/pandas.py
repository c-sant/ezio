import pandas as pd

from ..exception import InvalidFileFormat
from .base import BackendEngine


class PandasEngine(BackendEngine[pd.DataFrame]):
    """A class representing an engine for reading and writing tables using the
    Pandas library.

    This class extends the abstract BackendEngine class and provides concrete
    implementations for reading and writing tables of various sources and in
    different formats using Pandas.
    """

    @classmethod
    def save_table_as_file(cls, table: pd.DataFrame, table_data: dict, **kwargs):
        default_kwargs = {"index": False}
        default_kwargs.update(kwargs)

        file_path = table_data["path"]
        file_format = table_data["format"]

        match file_format:
            case "txt" | "csv":
                table.to_csv(file_path, **default_kwargs)
            case "excel":
                table.to_excel(file_path, **default_kwargs)
            case "json":
                table.to_json(file_path, **default_kwargs)
            case "parquet":
                table.to_parquet(file_path, **default_kwargs)
            case _:
                raise InvalidFileFormat(file_format)

    @classmethod
    def get_read_function(cls, file_format: str):
        match file_format:
            case "txt" | "csv":
                return pd.read_csv
            case "excel":
                return pd.read_excel
            case "json":
                return pd.read_json
            case "parquet":
                return pd.read_parquet
            case _:
                raise InvalidFileFormat(file_format)

    @classmethod
    def save_table_as_sql_table(
        cls, table: pd.DataFrame, table_data: dict, conn, **kwargs
    ):
        default_kwargs = {"index": False, "if_exists": "replace"}
        default_kwargs.update(kwargs)

        table_name = table_data["name"]

        table.to_sql(table_name, conn, **default_kwargs)

    @classmethod
    def load_table_from_sql_db(cls, query: str, conn, **kwargs) -> pd.DataFrame:
        table = pd.read_sql_query(query, conn, **kwargs)

        return table
