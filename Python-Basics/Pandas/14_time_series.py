# Pandas Time Series Analysis

import pandas as pd

# Create date range
dates = pd.date_range(start="2026-01-01", periods=7, freq="D")

# Create sample data
data = {
    "Date": dates,
    "Sales": [100, 150, 120, 180, 200, 170, 220]
}

df = pd.DataFrame(data)

# Display the dataset
print("Daily Sales Data:")
print(df)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract date components
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_Name"] = df["Date"].dt.day_name()

print("\nDate Components:")
print(df)

# Calculate total and average sales
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

# Filter sales greater than 150
print("\nSales Greater Than 150:")
print(df[df["Sales"] > 150])

# Set Date as index
df.set_index("Date", inplace=True)

# Resample weekly sales
weekly_sales = df["Sales"].resample("W").sum()

print("\nWeekly Sales:")
print(weekly_sales)
