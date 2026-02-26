import time

def benchmark_queries(conn, table_name):
    cursor = conn.cursor()
    queries = [f"SELECT COUNT(*) FROM {table_name}"]

    start = time.time()
    for q in queries:
        cursor.execute(q)
        cursor.fetchall()
    return round(time.time() - start, 4)

def create_index(conn, table_name, column):
    cursor = conn.cursor()
    cursor.execute(
        f"CREATE INDEX IF NOT EXISTS idx_{column} ON {table_name}({column})"
    )
    conn.commit()