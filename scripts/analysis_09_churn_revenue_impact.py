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

total_lost_mrr = churned["plan_mrr"].sum()

avg_lost_mrr = churned["plan_mrr"].mean()

print("\nCHURN REVENUE IMPACT")
print("=" * 50)

print(
    f"Total Monthly Revenue Lost : ₹{total_lost_mrr:,.2f}"
)

print(
    f"Average Revenue Per Churned Customer : ₹{avg_lost_mrr:,.2f}"
)