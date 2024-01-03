from .config import EzioConfig
from .source import get_data_source
from .type import TableLike


def load_table(layer: str, table_name: str, **kwargs) -> TableLike:
    """Load a table based on the specified layer and table name using the configured
    backend.

    Args:
        layer (str): The layer from which to load the table.
        table_name (str): The name of the table to load.
        **kwargs: Additional keyword arguments to be passed to the backend loader.

    Returns:
        DataFrame: The specified table as a DataFrame object. Object type depends
        on which backend engine is being used.

    Raises:
        KeyError: If the specified layer or table is not found in the configuration.
        InvalidSourceType: If the specified source type is not recognized.
        InvalidFileFormat: If the file format specified in the configuration is
        not recognized.
    """

    table_data = _get_table_data(layer, table_name)

    source_name = table_data["source"]
    source_data = _get_source_data(source_name)
    source = get_data_source(source_data)

    table = source.load_table(table_data, **kwargs)

    return table


def save_table(table: TableLike, layer: str, table_name: str, **kwargs):
    """Save a DataFrame table to a file based on the specified layer and table name.

    This function uses the configured backend engine to save a DataFrame table to
    a file based on the provided layer and table name. The file format and other
    configuration details are obtained from the specified layer and table in the
    configuration.

    Args:
        table (DataFrame): The DataFrame table to be saved.
        layer (str): The layer to which the table should be saved.
        table_name (str): The name of the table to be saved.
        **kwargs: Additional keyword arguments that can be passed to customize
        the saving process.

    Raises:
        KeyError: If the specified layer or table is not found in the configuration.
        InvalidSourceType: If the specified source type is not recognized.
        NotImplementedError: If the backend engine does not implement the required
        save method.
    """

    table_data = _get_table_data(layer, table_name)

    source_name = table_data["source"]
    source_data = _get_source_data(source_name)
    source = get_data_source(source_data)

    source.save_table(table, table_data, **kwargs)


def _get_table_data(layer: str, table_name: str) -> dict[str, str]:
    """
    Retrieve configuration data for a specified table in a given layer.

    Args:
        layer (str): The layer from which to retrieve the table configuration.
        table_name (str): The name of the table for which to retrieve configuration
        data.

    Returns:
        dict: A dictionary containing configuration data for the specified table.

    Raises:
        KeyError: If the specified layer or table is not found in the configuration.
    """

    try:
        data = EzioConfig.get(layer)[table_name]
        return data
    except KeyError as e:
        raise KeyError(
            f"Error loading table '{table_name}' from layer '{layer}'. "
            "Check if the table or layer exists in the config file."
        ) from e


def _get_source_data(source: str) -> str:
    """
    Retrieve the source type for a specified source.

    Args:
        source (str): The name of the source for which to retrieve the source type.

    Returns:
        str: The source type as specified in the configuration.

    Raises:
        KeyError: If the specified source is not found in the configuration.
    """

    try:
        data = EzioConfig.get("sources")[source]
        return data
    except KeyError as e:
        raise KeyError(
            f"Error loading source '{source}' type. "
            "Check if the source exists in the config file."
        ) from e
