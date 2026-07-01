import pandas as pd

print("LOADING FILES...")

customers = pd.read_csv(
    r"../Datasets/velocitypay_data/dim_customers.csv"
)

transactions = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_transactions.csv"
)

subs = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_subscriptions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

snapshot_date = (
    transactions["transaction_date"].max()
    + pd.Timedelta(days=1)
)

print("BUILDING RFM FEATURES...")

rfm = transactions.groupby(
    "customer_id"
).agg(
    Recency=(
        "transaction_date",
        lambda x: (snapshot_date - x.max()).days
    ),
    Frequency=(
        "transaction_id",
        "count"
    ),
    Monetary=(
        "transaction_amount",
        "sum"
    )
).reset_index()

print("MERGING DATASETS...")

ml_df = (
    customers
    .merge(rfm, on="customer_id", how="left")
    .merge(
        subs[
            [
                "customer_id",
                "plan_type",
                "renewal_count",
                "discount_pct",
                "is_churned"
            ]
        ],
        on="customer_id",
        how="left"
    )
)

print("\nDATASET SHAPE")
print(ml_df.shape)

print("\nTARGET DISTRIBUTION")
print(
    ml_df["is_churned"]
    .value_counts(dropna=False)
)

import os

os.makedirs("reports", exist_ok=True)

ml_df.to_csv(
    "reports/ml_dataset.csv",
    index=False
)

print("\nFILE SAVED")
print("reports/ml_dataset.csv")