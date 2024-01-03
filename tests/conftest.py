import pytest


@pytest.fixture(name="sample_config_path")
def sample_config_path_fixture() -> str:
    config_path = "sample_config.toml"

    with open(config_path, "w", encoding="utf-8") as file:
        file.write(
            """
            [element1]
            key1 = "value1"
            
            [element2]
            key2 = "value2"
            """
        )

    return config_path
