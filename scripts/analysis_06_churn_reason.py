import pandas as pd

subs = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_subscriptions.csv"
)

churned = subs[
    subs["is_churned"] == True
]

reason_summary = (
    churned.groupby("churn_reason")
    .size()
    .sort_values(ascending=False)
)

print("\nCHURN REASONS")
print("=" * 50)

print(reason_summary)