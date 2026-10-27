import numpy as np
import pandas as pd
import matplotlib.yplot as plt
import seaborn as sns  # Imported in the original notebook; optional for this analysis.

# Make the random sample reproducible
np.random.seed(42)
n = 1000

# Generate sample coffee-shop order data
dates = pd.date_range("2025-01-01", "2025-12-31")
df.info()

print("\n--- Raw numeric summary ---")
print(df.describe())

# Clean missing values BEFORE converting quantity to integer.
df["quantity"] = df["quantity"].fillna(df["quantity"].median()).round().astype(int)
df["unit_price"] = df["unit_price"].fillna(df["unit_price"].median())
df["payment"] = df["payment"].fillna("Unknown")

print("\n--- Missing values after cleaning ---")
print(df.isna().sum())

# Convert date to datetime and create date-based columns
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month_name()
df["month_number"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.day_name()

# Calculate sales and classify order size
df["Total_Sales"] = df["quantity"] * df["unit_price"]
df["Order_Size"] = np.where(df["quantity"] >= 4, "Bulk", "Regular")

print("\n--- Cleaned data (first 10 rows) ---")
print(df.head(10).to_string(index=False))

# Summary statistics using NumPy
sales = df["Total_Sales"]
print("\n--- Sales statistics ---")
print(f"Mean sale: {np.mean(sales):.2f}")
print(f"Median sale: {np.median(sales):.2f}")
print(f"Standard deviation: {np.std(sales):.2f}")
print(f"90th percentile sale: {np.percentile(sales, 90):.2f}")

# Business questions
print("\nBusiness insights ")

revenue_by_product = df.groupby("product")["Total_Sales"].sum().sort_values(ascending=False)
print(f"Product with maximum revenue: {revenue_by_product.idxmax()}")
print("\nRevenue by product:")
print(revenue_by_product.to_string())

# Sort months chronologically instead of alphabetically
monthly_revenue = (
    df.groupby("month_number")["Total_Sales"]
    .sum()
    .sort_index()
)
month_names = [pd.Timestamp(2025, month, 1).month_name() for month in monthly_revenue.index]
monthly_revenue.index = month_names

print(f"\nMonth with maximum revenue: {monthly_revenue.idxmax()}")
print("\nMonthly revenue:")
print(monthly_revenue.to_string())

payment_counts = df["payment"].value_counts()
print(f"\nMost used payment method: {payment_counts.idxmax()}")
print("\nPayment counts:")
print(payment_counts.to_string())

average_sales_by_day = df.groupby("day_of_week")["Total_Sales"].mean()
weekday_order = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]
average_sales_by_day = average_sales_by_day.reindex(weekday_order)
print(f"\nDay with highest average sale: {average_sales_by_day.idxmax()}")
print("\nAverage sales by day:")
print(average_sales_by_day.to_string())

# Visualizations
# 1. Line chart: monthly revenue
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker="o", color="red")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Total Monthly Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart: total revenue by product
plt.figure(figsize=(10, 6))
plt.bar(revenue_by_product.index, revenue_by_product.values)
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# 3. Histogram: distribution of order sales
plt.figure(figsize=(10, 6))
plt.hist(sales, bins=5, edgecolor="black")
plt.title("Distribution of Total Sales")
plt.xlabel("Sales per Order")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Pie chart: share of each payment method
plt.figure(figsize=(8, 8))
payment_counts.plot.pie(autopct="%1.1f%%", startangle=90, ylabel="")
plt.title("Share of Each Payment Method")
plt.tight_layout()
plt.show()

# Save the cleaned dataset beside this script
df.to_csv("coffee_analysis_cleaned.csv", index=False)
print("\nCleaned dataset saved as coffee_analysis_cleaned.csv")
