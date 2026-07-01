import pandas as pd

print("LOADING SUBSCRIPTIONS...")

subs = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_subscriptions.csv"
)

total_subs = len(subs)

churned = subs[
    subs["is_churned"] == True
]

churn_count = len(churned)

churn_rate = (
    churn_count / total_subs
) * 100

print("\nCHURN ANALYSIS")
print("=" * 50)

print(f"Total Subscriptions : {total_subs:,}")
print(f"Churned Customers   : {churn_count:,}")
print(f"Churn Rate          : {churn_rate:.2f}%")