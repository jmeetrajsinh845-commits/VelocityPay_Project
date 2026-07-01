import pandas as pd

customers = pd.read_csv(
    r"../Datasets/velocitypay_data/dim_customers.csv"
)

subs = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_subscriptions.csv"
)

churned = subs[
    subs["is_churned"] == True
]

merged = churned.merge(
    customers,
    on="customer_id",
    how="left"
)

industry_churn = (
    merged.groupby("industry_segment")
    .size()
    .sort_values(ascending=False)
)

print("\nCHURN BY INDUSTRY")
print("=" * 50)

print(industry_churn)