import os

import pandas as pd


def get_mock_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "product_id": [1000, 1001, 1002, 1003],
            "product_name": ["A", "B", "C", "D"],
            "price": [9.99, 11.30, 25.99, 150.00],
        }
    )


def create_data_folder():
    if not os.path.exists("data"):
        os.mkdir("data")


def mock_excel_table():
    create_data_folder()
    data = get_mock_data()
    data.to_excel("data/data.xlsx", index=False)


def mock_csv_table():
    create_data_folder()
    data = get_mock_data()
    data.to_csv("data/data.csv", index=False)


def mock_text_table():
    create_data_folder()
    data = get_mock_data()
    data.to_csv("data/data.txt", index=False)


def mock_json_table():
    create_data_folder()
    data = get_mock_data()
    data.to_json("data/data.json", index=False)


def mock_parquet_table():
    create_data_folder()
    data = get_mock_data()
    data.to_parquet("data/data.parquet", index=False)
