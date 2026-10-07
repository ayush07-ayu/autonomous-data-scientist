def profile_dataset(df):
    print("\n--- Dataset Profile ---")

    print("Total Rows:", df.shape[0])
    print("Total Columns:", df.shape[1])

    print("\nColumn Names:")
    print(df.columns.tolist())