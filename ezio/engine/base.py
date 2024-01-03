from abc import ABC, abstractmethod
from typing import Callable, Generic

from ..type import TableLike


class BackendEngine(ABC, Generic[TableLike]):
    """Abstract base class representing an interface for reading and writing tables
    from various sources and in different file formats.
    """

    @classmethod
    def load_table_from_file(cls, table_data: dict, **kwargs) -> TableLike:
        """Load a table from a file based on the provided configuration.

        This method is responsible for loading a table from a file using the specified
        backend and file format. It uses the provided `table_data` dictionary,
        which includes essential information such as the file path and format.

        Args:
            table_data (dict): A dictionary containing configuration information
            for the table. It should include at least 'path' (file path) and
            'format' (file format).
            **kwargs: Additional keyword arguments that can be passed to customize
            the loading process.

        Returns:
            DataFrame: The loaded table. The specific type may vary based on the
            backend implementation.
        """

        file_path = table_data["path"]
        file_format = table_data["format"]

        read_file = cls.get_read_function(file_format)
        table = read_file(file_path, **kwargs)

        return table

    @classmethod
    @abstractmethod
    def save_table_as_file(cls, table: TableLike, table_data: dict, **kwargs):
        """Save a table into a file in a local file system based on the provided
        configuration.

        Args:
            table (DataFrame): The tabular data.
            table_data (dict): A dictionary containing configuration information
            for the table. It should include at least 'path' (file path) and
            'format' (file format).
            **kwargs: Additional keyword arguments that can be passed to customize
            the saving process.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get_read_function(cls, file_format: str) -> Callable:
        """Get a read function corresponding to the file format specified.

        Args:
            file_format (str): The format of the file.

        Returns:
            Callable: A function that reads the specified file format using the
            current selected engine.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def save_table_as_sql_table(
        cls, table: TableLike, table_data: dict, conn, **kwargs
    ):
        """Save a DataFrame table to a SQL database table based on the provided
        configuration.

        Args:
            table (DataFrame): The DataFrame table to be saved.
            table_data (dict): A dictionary containing configuration information
            for the table.
            **kwargs: Additional keyword arguments that can be passed to customize
            the saving process.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def load_table_from_sql_db(cls, query: str, conn, **kwargs) -> TableLike:
        """Load a table from the data source based on the provided configuration.

        Args:
            table_data (dict): A dictionary containing configuration information
            for the table.
            **kwargs: Additional keyword arguments that can be passed to customize
            the loading process.

        Returns:
            DataFrame: The loaded DataFrame table.
        """

        raise NotImplementedError()
