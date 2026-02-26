import pandas as pd

# Load the CSV file (replace 'sales.csv' with your actual filename if different)
sales_df = pd.read_csv("sales.csv")

# Convert the 'Sales' column to numeric values; if non-numeric (like dates), convert to NaN
sales_df['Sales'] = pd.to_numeric(sales_df['Sales'], errors='coerce')

# Fill missing (NaN) values with the mean of valid numbers
sales_df['Sales'].fillna(sales_df['Sales'].mean(), inplace=True)

# Save the cleaned data to a new CSV file
sales_df.to_csv("sales_cleaned.csv", index=False)

print("✅ Missing sales values filled successfully and saved to 'sales_cleaned.csv'")