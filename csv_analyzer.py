# Import pandas for easy CSV manipulation
import pandas as pd

def analyze_csv(filepath):
    # Try to load and analyze the CSV data
    try:
        data = pd.read_csv(filepath)
        print("Preview of data:")
        print(data.head())

        print("\nData Summary:")
        print(data.describe())

        print("\nMissing values by column:")
        print(data.isna().sum())

        print("\nUnique value count by column:")
        print(data.nunique())
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        analyze_csv(sys.argv[1])
    else:
        print("Usage: python csv_analyzer.py <path_to_csv>")
