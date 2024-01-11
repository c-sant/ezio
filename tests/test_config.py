import pytest

from ezio.config import EzioConfig, load_config_from_file, set_engine
from ezio.engine.pandas import PandasEngine
from ezio.exception import InvalidBackendEngineError


def test_load_config_function(sample_config_path: str):
    load_config_from_file(sample_config_path)
    assert EzioConfig._config_tree == {
        "element1": {"key1": "value1"},
        "element2": {"key2": "value2"},
    }


def test_load_config_class_method(sample_config_path: str):
    EzioConfig.load_from_file(sample_config_path)
    assert EzioConfig._config_tree == {
        "element1": {"key1": "value1"},
        "element2": {"key2": "value2"},
    }


def test_load_config_function_with_invalid_path_should_raise_error():
    with pytest.raises(FileNotFoundError):
        load_config_from_file("nonexistent_file.toml")


def test_load_config_class_method_with_invalid_path_should_raise_error():
    with pytest.raises(FileNotFoundError):
        EzioConfig.load_from_file("nonexistent_file.toml")


@pytest.mark.parametrize(
    ("element", "result"),
    [
        ("element1", {"key1": "value1"}),
        ("element2", {"key2": "value2"}),
    ],
)
def test_get_element_from_config_tree(
    sample_config_path: str, element: str, result: dict[str, str]
):
    load_config_from_file(sample_config_path)

    assert EzioConfig.get(element) == result


def test_get_should_return_none_when_element_is_missing(sample_config_path: str):
    load_config_from_file(sample_config_path)

    assert EzioConfig.get("nonexistent_element") is None


def test_pandas_should_be_the_default_engine():
    assert EzioConfig.get_engine() == PandasEngine


@pytest.mark.parametrize(
    ("engine_name", "engine"),
    [
        ("pandas", PandasEngine),
    ],
)
def test_set_engine_function(engine_name: str, engine: type):
    set_engine(engine_name)

    assert EzioConfig.get_engine() == engine


@pytest.mark.parametrize("engine", [PandasEngine])
def test_set_engine_class_method(engine: type):
    EzioConfig.set_engine(engine)

    assert EzioConfig.get_engine() == engine


def test_set_engine_function_with_invalid_engine_should_raise_error():
    with pytest.raises(InvalidBackendEngineError):
        set_engine("invalid_engine")


@pytest.mark.parametrize("invalid_type", [int, str, float, bool, list, dict])
def test_set_engine_class_method_with_invalid_engine_should_raise_error(
    invalid_type: type,
):
    with pytest.raises(TypeError):
        EzioConfig.set_engine(invalid_type)
