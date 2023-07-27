import pandas as pd

# Reading data from an Excel file
df = pd.read_excel("data.xlsx")

# Display the first few rows of the DataFrame
print("Original Data:")
print(df.head())

# Data Cleaning: Handling Missing Values
print("\nData Cleaning: Handling Missing Values")
print("Number of Missing Values in each Column:")
print(df.isnull().sum())

# Fill missing values in 'Age' column with the mean
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

# Drop rows with missing values in 'Salary' column
df.dropna(subset=['Salary'], inplace=True)

# Data Wrangling: Adding a new column
df['Bonus'] = df['Salary'] * 0.1

# Data Wrangling: Filtering Data
filtered_df = df[df['Age'] >= 30]

# Data Wrangling: Grouping and Aggregating Data
grouped_df = df.groupby('Department')['Salary'].mean().reset_index()

# Writing the cleaned and processed data to a new Excel file
df.to_excel("cleaned_data.xlsx", index=False)

# Displaying the cleaned and processed DataFrame
print("\nCleaned and Processed Data:")
print(df.head())

# Displaying the filtered DataFrame
print("\nFiltered Data (Age >= 30):")
print(filtered_df)

# Displaying the grouped and aggregated DataFrame
print("\nGrouped and Aggregated Data:")
print(grouped_df)
