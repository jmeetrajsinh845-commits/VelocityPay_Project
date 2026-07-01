import pandas as pd

print("LOADING DATA...")

transactions = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_transactions.csv"
)

failed_txn = transactions[
    transactions["payment_status"] == "FAILED"
]

failed_amount = failed_txn[
    "transaction_amount"
].sum()

failed_count = len(failed_txn)

print("\nREVENUE LEAKAGE ANALYSIS")
print("=" * 50)

print(f"Failed Transactions : {failed_count:,}")

print(
    f"Potential Revenue Lost : ₹{failed_amount:,.2f}"
)