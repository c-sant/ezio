from abc import ABC, abstractmethod

from ..type import TableLike


class DataSource(ABC):
    """Abstract base class representing a data source for loading and saving tables."""

    @abstractmethod
    def load_table(self, table_data: dict, **kwargs) -> TableLike:
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

    @abstractmethod
    def save_table(self, table: TableLike, table_data: dict, **kwargs):
        """Save a DataFrame table to the data source based on the provided configuration.

        Args:
            table (DataFrame): The DataFrame table to be saved.
            table_data (dict): A dictionary containing configuration information
            for the table.
            **kwargs: Additional keyword arguments that can be passed to customize
            the saving process.
        """

        raise NotImplementedError()
