def auto_score_numeric(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if not numeric_cols:
        return df

    col = numeric_cols[0]
    df['auto_score'] = df[col] / df[col].max()

    return df