import pandas as pd
import matplotlib.pyplot as plt

# Load your sales CSV file
sales_df = pd.read_csv("sales.csv")  # Change filename if different

# Convert 'Date' column to datetime
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

#convert 'Sales' column to numeric
sales_df['Sales'] = pd.to_numeric(sales_df['Sales'], errors='coerce')

# Sort by date
sales_df = sales_df.sort_values('Date')

# Set Date as index (optional but good for plotting)
sales_df.set_index('Date', inplace=True)

# --- Trend Analysis ---
print("Total Sales:", sales_df['Sales'].sum())
print("Average Sales:", sales_df['Sales'].mean())
print("Maximum Sale:", sales_df['Sales'].max())
print("Minimum Sale:", sales_df['Sales'].min())
print("Number of Missing Sales:", sales_df['Sales'].isnull().sum())

# --- Plot Sales Trend ---
plt.figure(figsize=(10, 5))
plt.plot(sales_df.index, sales_df['Sales'], marker='o', linestyle='-', color='blue')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("sales_trend.png")  # Save image
plt.show()