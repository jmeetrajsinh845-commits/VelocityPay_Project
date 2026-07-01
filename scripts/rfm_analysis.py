import pandas as pd

print("LOADING TRANSACTIONS...")

transactions = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Reference date
snapshot_date = (
    transactions["transaction_date"].max()
    + pd.Timedelta(days=1)
)

print("Snapshot Date:", snapshot_date)

# RFM Metrics
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
)

print("\nRFM TABLE")
print("=" * 50)

print(rfm.head())

print("\nTotal Customers:")
print(len(rfm))
print("\nCREATING RFM SCORES...")

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5,4,3,2,1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1,2,3,4,5]
)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

print("\nRFM SCORES")
print("=" * 50)

print(
    rfm[
        [
            "Recency",
            "Frequency",
            "Monetary",
            "R_Score",
            "F_Score",
            "M_Score",
            "RFM_Score"
        ]
    ].head()
)
print("\nCREATING CUSTOMER SEGMENTS...")

def segment_customer(row):

    if row["R_Score"] >= 4 and row["F_Score"] >= 4:
        return "Champions"

    elif row["R_Score"] >= 3 and row["F_Score"] >= 3:
        return "Loyal Customers"

    elif row["R_Score"] >= 4:
        return "Potential Loyalists"

    elif row["R_Score"] <= 2 and row["F_Score"] <= 2:
        return "At Risk"

    else:
        return "Others"

rfm["Segment"] = rfm.apply(
    segment_customer,
    axis=1
)

segment_summary = (
    rfm["Segment"]
    .value_counts()
)

print("\nCUSTOMER SEGMENTS")
print("=" * 50)

print(segment_summary)

import os

os.makedirs("reports", exist_ok=True)

rfm.to_csv("reports/rfm_customers.csv")