import pandas as pd
import numpy as np

# 1. E-Commerce Sales & Profitability Dataset Creation
data = {
    'Order_ID': ['ORD-501', 'ORD-502', 'ORD-503', 'ORD-504', 'ORD-505', 'ORD-506'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home Decor', 'Clothing', 'Home Decor'],
    'Sales_INR': [45000, 12000, 85000, 25000, 8000, 35000],
    'Discount_%': [10, 25, 5, 30, 40, 15],
    'Profit_INR': [8000, -1200, 18000, -3000, -1500, 5000]
}

df_sales = pd.DataFrame(data)

# 2. Profit Margin & Loss Analysis Metrics
df_sales['Net_Revenue'] = df_sales['Sales_INR'] * (1 - df_sales['Discount_%'] / 100)
df_sales['Profit_Margin_%'] = (df_sales['Profit_INR'] / df_sales['Sales_INR']) * 100
df_sales['Profit_Status'] = np.where(df_sales['Profit_INR'] < 0, 'LOSS MAKING', 'PROFITABLE')

print("--- E-Commerce Category Performance Summary ---")
print(df_sales[['Order_ID', 'Category', 'Sales_INR', 'Profit_Margin_%', 'Profit_Status']])

# 3. Export CSV Report
df_sales.to_csv('ecommerce_sales_report.csv', index=False)
print("\nReport successfully saved as 'ecommerce_sales_report.csv'")
