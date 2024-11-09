import pandas as pd

# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [1500, 1200, 1700, 1300],
    'Profit': [300, 200, 400, 250]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Calculate total sales and average profit
total_sales = df['Sales'].sum()
average_profit = df['Profit'].mean()

print(f"\nTotal Sales: {total_sales}")
print(f"Average Profit: {average_profit}")

# Filter products with sales greater than 1300
high_sales = df[df['Sales'] > 1300]
print("\nProducts with High Sales:")
print(high_sales)
