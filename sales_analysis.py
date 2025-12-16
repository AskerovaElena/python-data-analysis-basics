import pandas as pd

data = {
    "Region": ["Baku", "Ganja", "Sumgait", "Baku", "Ganja"],
    "Product": ["Laptop", "Phone", "Tablet", "Phone", "Laptop"],
    "Sales": [1200, 800, 600, 950, 1100]
}

df = pd.DataFrame(data)

total_sales = df.groupby("Region")["Sales"].sum()

print("Total sales by region:")
print(total_sales)
