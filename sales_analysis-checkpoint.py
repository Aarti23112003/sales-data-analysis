import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Dataset shape:", df.shape)
print("\nTotal Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nTop Products:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()
