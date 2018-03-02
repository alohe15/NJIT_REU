#NJIT Research Application Program
#Arnav Lohe, arnavlohe15@gmail.com

def load_csv(str1):
    import pandas as pd
    df = pd.read_csv(str1)
    return df

def find_sums(m, n, df):
    row_count = len(df.index)
    for i in range(0, row_count):
        if df["Customer Account"][i] == "C001":
            m += df["Total Purchase Value"][i]
        if df["Customer Account"][i] == "C002":
            n += df["Total Purchase Value"][i]
    return[m, n]

def output(lst):
    m = lst[0]
    m = str(float("{0:.2f}".format(m)))
    n = lst[1]
    n = str(float("{0:.2f}".format(n)))
    print("Customer 1's total aggregate purchases are $" + m + " and Customer 2's aggregate purchases are $" + n)

df = load_csv("supermarket_test.csv")
df["Total Purchase Value"] = df["Quantity"] * df["Sale Price Per Unit"]
sum_customer1 = sum_customer2 = 0.0
lst = find_sums(sum_customer1, sum_customer2, df)
output(lst)
