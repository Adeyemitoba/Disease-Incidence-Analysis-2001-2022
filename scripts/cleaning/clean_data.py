import pandas as pd

# Load the raw data
raw_data_path = 'data/raw/raw_data.csv'
processed_data_path = 'data/processed/cleaned_data.csv'

print("Loading raw data...")
df = pd.read_csv(raw_data_path)

# Basic cleaning steps
print("Cleaning data...")

# Drop rows with missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize text to lowercase in a specific column (e.g., 'disease')
if 'disease' in df.columns:
    df['disease'] = df['disease'].str.lower()

# Save cleaned data
print("Saving cleaned data...")
df.to_csv(processed_data_path, index=False)

print("Data cleaning complete. Cleaned data saved to:", processed_data_path)
