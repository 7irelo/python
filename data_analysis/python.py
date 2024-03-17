import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])

sales.head()
sales['Customer_Age'].mean()
sales['Customer_Age'].plot(kind='kde', figsize=(14,6))
sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14,6))
sales.describe()