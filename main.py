from config import DB_NAME, TABLE_NAME, DATA_FILE
from core.database import load_dataset, store_dataframe, get_connection
from core.scoring import auto_score_numeric
from core.optimization import benchmark_queries, create_index

def main():
    # Load
    df = load_dataset(DATA_FILE)

    # Score
    df = auto_score_numeric(df)

    # Store
    store_dataframe(df, DB_NAME, TABLE_NAME)

    conn = get_connection(DB_NAME)

    # Before optimization
    before = benchmark_queries(conn, TABLE_NAME)
    print("Before:", before, "seconds")

    # Create index on first numeric column
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if numeric_cols:
        create_index(conn, TABLE_NAME, numeric_cols[0])

    # After optimization
    after = benchmark_queries(conn, TABLE_NAME)
    print("After:", after, "seconds")
    
    #Difference b/w Before and After
    print("Diff between Before & After: ",before-after)

    conn.close()

if __name__ == "__main__":
    main()