import pandas as pd

# Use the provided file path
file_path = 'C:\\Users\\snarc\\Documents\\Disease-Incidence-Analysis-2001-2022\\Infectious Diseases by disease, county, year and sex.csv'

# Load the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Display information about the dataset
print(data.info())
# Display the first few rows
print(data.head())

# Display data types and missing values
print(data.info())

# Display summary statistics
print(data.describe(include='all'))
# Check for missing values in each column
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)
# Example: Fill missing values with 0 in specific columns
data['Cases'].fillna(0, inplace=True)
data['Lower_95_CI'].fillna(0, inplace=True)
data['Upper_95_CI'].fillna(0, inplace=True)

# Alternatively, you could fill with mean/median:
# data['Cases'].fillna(data['Cases'].mean(), inplace=True)
# Check for duplicates
duplicate_rows = data.duplicated().sum()
print("Number of duplicate rows:", duplicate_rows)

# Remove duplicate rows if any
data.drop_duplicates(inplace=True)
# Example: Fill missing values with 0 in specific columns
data['Cases'] = data['Cases'].fillna(0)
if 'Lower_95_CI' in data.columns:
    data['Lower_95_CI'] = data['Lower_95_CI'].fillna(0)
else:
    print("Column 'Lower_95_CI' not found in the dataset.")

# Alternatively, you could fill with mean/median:
# data['Cases'].fillna(data['Cases'].mean(), inplace=True)
# Check if 'Cases' column exists and fill NaN values
if 'Cases' in data.columns:
    data['Cases'] = data['Cases'].fillna(0)
else:
    print("Column 'Cases' not found in the dataset.")

# Check if 'Lower_95_CI' column exists and fill NaN values
if 'Lower_95_CI' in data.columns:
    data['Lower_95_CI'] = data['Lower_95_CI'].fillna(0)
else:
    print("Column 'Lower_95_CI' not found in the dataset.")
# Convert the Year column to datetime (if it's a date)
# Assuming the Year column is numeric but should be a date
# Uncomment the line below if you want to convert
# data['Year'] = pd.to_datetime(data['Year'], format='%Y')
data['Lower_95_CI'] = data.get('Lower_95_CI', pd.Series([0]*len(data)))
print(data.columns)
print("Columns in data:", data.columns)
# Safely fill NaNs in 'Lower_95_CI' if it exists, otherwise create the column with 0s
data['Lower_95_CI'] = data.get('Lower_95_CI', pd.Series([0] * len(data)))
# Ensure 'Cases' column exists and fill NaNs if it does
if 'Cases' in data.columns:
    data['Cases'] = data['Cases'].fillna(0)
else:
    print("Column 'Cases' not found in the dataset.")

# Ensure 'Lower_95_CI' column exists before filling NaNs
if 'Lower_95_CI' in data.columns:
    data['Lower_95_CI'] = data['Lower_95_CI'].fillna(0)
else:
    print("Column 'Lower_95_CI' not found in the dataset.")
import pandas as pd

# Load the CSV file
file_path = 'C:\\Users\\snarc\\Documents\\Disease-Incidence-Analysis-2001-2022\\Infectious Diseases by disease, county, year and sex.csv'
data = pd.read_csv(file_path)

# Get the number of attributes (columns) and records (rows)
num_attributes = data.shape[1]
num_records = data.shape[0]

print("Number of attributes (columns):", num_attributes)
print("Number of records (rows):", num_records)
