import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned sales data
sales_df = pd.read_csv("sales.csv")

# Convert sales to numeric
sales_df['Sales'] = pd.to_numeric(sales_df['Sales'], errors='coerce')

# Convert Date to datetime (if not already)
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# Sort by date
sales_df = sales_df.sort_values('Date')

# Calculate 3-day moving average
sales_df['Moving_Avg'] = sales_df['Sales'].rolling(window=3).mean()

# Plot the trend
plt.figure(figsize=(10, 5))
plt.plot(sales_df['Date'], sales_df['Sales'], label='Actual Sales', marker='o')
plt.plot(sales_df['Date'], sales_df['Moving_Avg'], label='3-Day Moving Avg', color='orange')

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trend with Moving Average")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()