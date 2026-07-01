import pandas as pd

print("LOADING DATA...")

transactions = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

transactions["month"] = (
    transactions["transaction_date"]
    .dt.to_period("M")
)

monthly_revenue = (
    transactions
    .query("payment_status == 'SUCCESS'")
    .groupby("month")
    .agg(
        revenue=("transaction_amount", "sum")
    )
)

print("\nMONTHLY REVENUE")
print(monthly_revenue.tail(12))