from pandas.testing import assert_frame_equal

from ezio import load_config, load_table

from .mock import (
    get_mock_data,
    mock_csv_table,
    mock_excel_table,
    mock_json_table,
    mock_parquet_table,
    mock_text_table,
)


def test_load_table_from_excel_file(config_path: str):
    load_config(config_path)
    mock_excel_table()

    expected = get_mock_data()
    result = load_table("test", "excel")

    assert_frame_equal(expected, result)


def test_load_table_from_csv_file(config_path: str):
    load_config(config_path)
    mock_csv_table()

    expected = get_mock_data()
    result = load_table("test", "csv")

    assert_frame_equal(expected, result)


def test_load_table_from_txt_file(config_path: str):
    load_config(config_path)
    mock_text_table()

    expected = get_mock_data()
    result = load_table("test", "text")

    assert_frame_equal(expected, result)


def test_load_table_from_json_file(config_path: str):
    load_config(config_path)
    mock_json_table()

    expected = get_mock_data()
    result = load_table("test", "json")

    assert_frame_equal(expected, result)


def test_load_table_from_parquet_file(config_path: str):
    load_config(config_path)
    mock_parquet_table()

    expected = get_mock_data()
    result = load_table("test", "parquet")

    assert_frame_equal(expected, result)
