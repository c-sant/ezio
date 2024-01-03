import toml

from .engine import BackendEngine, PandasEngine
from .exception import ConfigNotLoadedException, InvalidBackendEngineError


class EzioConfig:
    """
    A class representing the configuration for EzIO.

    This class provides methods to load and retrieve configuration settings for
    tables.
    """

    _config_tree = {}
    _engine = PandasEngine

    @classmethod
    def load_config(cls, config_file_path: str):
        """Load the configuration from a TOML file.

        Args:
            config_file_path (str): The path to the TOML configuration file.
        """

        cls._config_tree = toml.load(config_file_path)

    @classmethod
    def get(cls, element: str) -> dict:
        """Retrieve the configuration settings for a specific element.

        Args:
            element (str): The element for which to retrieve configuration settings.

        Returns:
            dict: The configuration settings for the specified element.

        Raises:
            ConfigNotLoadedException: If the configuration has not been loaded.
        """

        if not cls._config_tree:
            raise ConfigNotLoadedException()

        return cls._config_tree.get(element)

    @classmethod
    def get_engine(cls) -> BackendEngine:
        """Get the configured backend engine used by EzIO methods and classes.

        Returns:
            BackendEngine: The class with backend methods used by EzIO methods
            and classes.
        """

        return cls._engine

    @classmethod
    def set_engine(cls, engine: BackendEngine):
        """Set the backend engine to be used by EzIO methods and classes.

        Args:
            engine (BackendEngine): The class with backend methods to be used.

        Raises:
            TypeError: If the specified engine is not a subclass of BackendEngine.
        """

        if not issubclass(engine, BackendEngine):
            raise TypeError(f"incorrect subclass for engine: '{type(engine)}'.")

        cls._engine = engine


def load_config(config_file_path: str):
    """Load the EzIO configuration from a TOML file.

    Args:
        config_file_path (str): The path to the TOML configuration file.
    """

    EzioConfig.load_config(config_file_path)


def set_engine(new_engine: str):
    """Switch the backend engine used by EzIO based on the specified engine name.

    Args:
        new_engine (str): The name of the new backend engine. Supported values:
        "pandas", "polars".

    Raises:
        InvalidBackendEngineError: If the specified engine name is not supported.
    """

    match new_engine:
        case "pandas":
            EzioConfig.set_engine(PandasEngine)
        case _:
            raise InvalidBackendEngineError(new_engine)
