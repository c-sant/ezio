import textwrap

import pytest


@pytest.fixture(name="sample_config_path")
def sample_config_path_fixture() -> str:
    config_path = "sample_config.toml"

    with open(config_path, "w", encoding="utf-8") as file:
        file.write(
            textwrap.dedent(
                """
            [element1]
            key1 = "value1"
            
            [element2]
            key2 = "value2"
            """
            )
        )

    return config_path


@pytest.fixture(name="config_path")
def config_path_fixture() -> str:
    config_path = "config.toml"

    with open(config_path, "w", encoding="utf-8") as file:
        file.write(
            textwrap.dedent(
                """
            [sources.localStorage]
            type = "localFileSystem"

            [test.excel]
            path = "data.xlsx"
            source = "localStorage"
            format = "excel"

            [test.csv]
            path = "data.csv"
            source = "localStorage"
            format = "csv"

            [test.text]
            path = "data.txt"
            source = "localStorage"
            format = "txt"

            [test.json]
            path = "data.json"
            source = "localStorage"
            format = "json"

            [test.parquet]
            path = "data.parquet"
            source = "localStorage"
            format = "parquet"
            """
            )
        )

    return config_path
