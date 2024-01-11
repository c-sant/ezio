from ..exception import InvalidSourceType
from .base import DataSource
from .local_directory import LocalDirectoryDataSource


def get_data_source(source_metadata: dict) -> DataSource:
    """Factory function to create a data source instance based on the specified
    source type.

    Args:
        source_metadata (dict): Data related to the source type and configurations.

    Returns:
        DataSource: An instance of the appropriate data source class.

    Raises:
        InvalidSourceType: If the specified source type is not supported.
    """

    source_type = source_metadata["type"]

    match source_type:
        case "localDirectory":
            local_directory_path = source_metadata["path"]
            return LocalDirectoryDataSource(local_directory_path)
        case _:
            raise InvalidSourceType(source_type)
