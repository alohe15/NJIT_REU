#NJIT Research Application Program
#Arnav Lohe, arnavlohe15@gmail.com

import pandas as pd
df = pd.read_csv("supermarket_test.csv")
df["Total Purchase Value"] = df["Quantity"] * df["Sale Price Per Unit"]
sum_customer1 = sum_customer2 = 0.0
row_count = len(df.index)
for i in range(0, row_count):
    if df["Customer Account"][i] == "C001":
        sum_customer1 += df["Total Purchase Value"][i]
    if df["Customer Account"][i] == "C002":
        sum_customer2 += df["Total Purchase Value"][i]
sum_customer1 = str(float("{0:.2f}".format(sum_customer1)))
sum_customer2 = str(float("{0:.2f}".format(sum_customer2)))
print(sum_customer1)
print(sum_customer2)
print("Customer 1's total aggregate purchases are $" + sum_customer1 + " and Customer 2's aggregate purchases are $" + sum_customer2)
