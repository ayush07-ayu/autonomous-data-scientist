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

    print("\nNumeric Statistics:")
    print(df.select_dtypes(include="number").describe())

    print("\nCategorical Value Counts:")

    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:
     print(f"\n{column}:")
     print(df[column].value_counts().head(10))

     print("\nPotential Date Columns:")

    for column in df.columns:
     if "date" in column.lower():
          print(column)

    print("\n--- Profiling Summary ---")

    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing Values:", df.isnull().sum().sum())
    print("Duplicate Rows:", df.duplicated().sum())
    print("Numeric Columns:", len(df.select_dtypes(include="number").columns))
    print("Categorical Columns:", len(df.select_dtypes(include="object").columns))
