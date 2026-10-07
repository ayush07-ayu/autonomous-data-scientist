import pandas as pd
from src.profiling.profiler import profile_dataset

def load_dataset(file_path):
    df = pd.read_csv(file_path)

    print("Dataset loaded successfully!")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())    

    print("\nBasic Statistics:")
    print(df.describe())
    
    profile_dataset(df)
    return df


if __name__ == "__main__":
    load_dataset("data/raw/sales.csv")