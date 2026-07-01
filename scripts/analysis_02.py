import pandas as pd

print("LOADING TRANSACTIONS...")

transactions = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_transactions.csv"
)

status_summary = (
    transactions.groupby("payment_status")
    .agg(
        total_transactions=("transaction_id", "count")
    )
)

print("\nTRANSACTION STATUS SUMMARY")
print(status_summary)

success_rate = (
    transactions["payment_status"]
    .eq("SUCCESS")
    .mean()
    * 100
)

print(f"\nSUCCESS RATE = {success_rate:.2f}%")