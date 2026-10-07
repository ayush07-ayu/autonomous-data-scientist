def profile_dataset(df):
    print("\n--- Dataset Profile ---")

    print("Total Rows:", df.shape[0])
    print("Total Columns:", df.shape[1])

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nMissing Value Percentage:")
    print((df.isnull().sum() / len(df)) * 100)

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)

    print("\nUnique Values:")
    print(df.nunique())

    print("\nNumeric Columns:")
    print(df.select_dtypes(include="number").columns.tolist())

    print("\nCategorical Columns:")
    print(df.select_dtypes(include="object").columns.tolist())