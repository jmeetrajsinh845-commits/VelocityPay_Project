import pandas as pd

customers = pd.read_csv(
    r"../Datasets/velocitypay_data/dim_customers.csv"
)

industry_summary = (
    customers.groupby("industry_segment")
    .agg(
        total_customers=("customer_id", "count")
    )
    .sort_values(
        by="total_customers",
        ascending=False
    )
)

print("\nINDUSTRY DISTRIBUTION")
print(industry_summary)