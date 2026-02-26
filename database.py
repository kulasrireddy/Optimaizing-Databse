import sqlite3
import pandas as pd

def load_dataset(file_path):
    if file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    elif file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format")

def store_dataframe(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def get_connection(db_name):
    return sqlite3.connect(db_name)