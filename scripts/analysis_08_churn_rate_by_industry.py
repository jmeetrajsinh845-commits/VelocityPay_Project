import pandas as pd

customers = pd.read_csv(
    r"../Datasets/velocitypay_data/dim_customers.csv"
)

subs = pd.read_csv(
    r"../Datasets/velocitypay_data/fact_subscriptions.csv"
)

merged = subs.merge(
    customers,
    on="customer_id",
    how="left"
)

industry_summary = (
    merged.groupby("industry_segment")
    .agg(
        total_subs=("subscription_id", "count"),
        churned=("is_churned", "sum")
    )
)

industry_summary["churn_rate"] = (
    industry_summary["churned"]
    / industry_summary["total_subs"]
) * 100

industry_summary = industry_summary.sort_values(
    by="churn_rate",
    ascending=False
)

print("\nCHURN RATE BY INDUSTRY")
print("=" * 60)

print(industry_summary)