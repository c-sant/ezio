class InvalidBackendEngineError(Exception):
    """Exception raised when an invalid backend engine is specified for loading
    or saving tables.

    Attributes:
        backend_engine (str): The backend engine that caused the error.
    """

    def __init__(self, backend_engine: str):
        super().__init__(f"Invalid backend engine: {backend_engine}")
        self.backend_engine = backend_engine


class InvalidFileFormat(Exception):
    """Exception raised when an invalid file format is specified for table loading.

    Attributes:
        file_format (str): The invalid file format that caused the error.
    """

    def __init__(self, file_format: str):
        super().__init__(f"Invalid file format: {file_format}")
        self.format_type = file_format


class InvalidSourceType(Exception):
    """Exception raised when an invalid source type is specified.

    Attributes:
        source_type (str): The invalid source type that caused the error.
    """

    def __init__(self, source_type: str):
        super().__init__(f"Invalid source type: {source_type}")
        self.source_type = source_type


class ConfigNotLoadedException(Exception):
    """Exception raised when attempting to access configuration without loading it."""

    def __init__(
        self, message: str = "Attempted to access configuration without loading it."
    ):
        super().__init__(message)
        self.message = message


class InvalidSQLiteDatabasePath(Exception):
    """Exception raised when an invalid path is passed for a SQLite database file."""

    def __init__(self, db_path: str):
        super().__init__(f"Invalid SQLite database path: {db_path}")
        self.db_path = db_path
