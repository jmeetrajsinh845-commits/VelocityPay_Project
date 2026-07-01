"""
VelocityPay Financial Technologies — Synthetic Dataset Generator
================================================================
Generates all 5 interconnected tables for the analytics warehouse.
All tables share consistent customer_ids. Referential integrity enforced.

Output: 5 CSV files ready for database seeding.
Run:    python generate_velocitypay_data.py

Approx output sizes:
  dim_customers       -> 10,000 rows
  fact_transactions   -> ~180,000 rows  (18 avg txns/customer)
  fact_subscriptions  -> ~10,500 rows
  fact_loan_accounts  -> ~4,000 rows
  fact_product_usage  -> ~120,000 rows  (daily snapshots, 12 rows/customer)
"""

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta, date
import random
import uuid
import os

fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
N_CUSTOMERS      = 10_000
START_DATE       = date(2023, 1, 1)
END_DATE         = date(2026, 3, 31)
MONTHLY_CHURN    = 0.058   # 5.8% monthly churn rate
LOAN_COVERAGE    = 0.40    # 40% of customers have a loan
OUTPUT_DIR       = "velocitypay_data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

CITIES = [
    ("Mumbai","Maharashtra","T1"), ("Delhi","Delhi","T1"),
    ("Bengaluru","Karnataka","T1"), ("Hyderabad","Telangana","T1"),
    ("Chennai","Tamil Nadu","T1"), ("Pune","Maharashtra","T1"),
    ("Ahmedabad","Gujarat","T1"), ("Kolkata","West Bengal","T1"),
    ("Jaipur","Rajasthan","T2"), ("Surat","Gujarat","T2"),
    ("Lucknow","Uttar Pradesh","T2"), ("Kanpur","Uttar Pradesh","T2"),
    ("Nagpur","Maharashtra","T2"), ("Indore","Madhya Pradesh","T2"),
    ("Coimbatore","Tamil Nadu","T2"), ("Bhopal","Madhya Pradesh","T2"),
    ("Patna","Bihar","T3"), ("Agra","Uttar Pradesh","T3"),
    ("Varanasi","Uttar Pradesh","T3"), ("Meerut","Uttar Pradesh","T3"),
    ("Nashik","Maharashtra","T3"), ("Rajkot","Gujarat","T3"),
]

INDUSTRY_SEGMENTS = [
    "Retail_Fashion","Retail_Electronics","Retail_Grocery",
    "Food_Beverage","Healthcare_Pharmacy","Education_EdTech",
    "Logistics_Transport","Manufacturing_SME","Tech_Startup",
    "Professional_Services","Travel_Hospitality","Auto_Dealership",
    "Construction_Real_Estate","Financial_Services","Media_Entertainment",
]

ACQUISITION_CHANNELS = [
    "Inside_Sales","Digital_Organic","Partner_Referral",
    "Inbound_Web","Field_Sales","Agency","Event","Freemium_Upgrade"
]

PLANS = [
    ("Starter",  1999,  "Monthly"),
    ("Starter",  19990, "Annual"),
    ("Growth",   4999,  "Monthly"),
    ("Growth",   49990, "Annual"),
    ("Enterprise",12999,"Monthly"),
    ("Enterprise",129990,"Annual"),
]

TRANSACTION_TYPES = ["UPI","NEFT","IMPS","Card_Debit","Card_Credit","BNPL","Wallet","RTGS"]
FAILURE_REASONS   = [
    "INSUFFICIENT_FUNDS","BANK_TIMEOUT","INVALID_VPA",
    "TRANSACTION_LIMIT_EXCEEDED","DUPLICATE_TRANSACTION",
    "CARD_DECLINED","NETWORK_ERROR","FRAUD_SUSPECTED"
]
MCC_CODES = ["5411","5812","5912","7011","5621","4121","5734","5999","7389","8011"]

CHURN_REASONS = [
    "Switched to competitor","Too expensive","Product missing features",
    "Poor customer support","Business closed","Integration issues",
    "Settlement delays","Better deal elsewhere", None, None  # Nulls = no exit survey
]

LOAN_TYPES = ["WorkingCapital","TermLoan","BNPL_Merchant","MachineryLoan","InvoiceDiscounting"]
LOAN_STATUSES = ["ACTIVE","CLOSED","NPA","RESTRUCTURED"]

print("Generating dim_customers ...")
# ─────────────────────────────────────────────
# TABLE 1 — dim_customers
# ─────────────────────────────────────────────
customer_ids = [f"VP_C_{i:08d}" for i in range(1, N_CUSTOMERS + 1)]

city_data    = [random.choice(CITIES) for _ in range(N_CUSTOMERS)]
cities       = [c[0] for c in city_data]
states       = [c[1] for c in city_data]
tiers        = [c[2] for c in city_data]

onboarding_dates = [
    START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days - 180))
    for _ in range(N_CUSTOMERS)
]

# Tier 1 customers get segment labels; ~4% of T1/T2 missing (data quality issue)
def assign_segment(tier):
    if tier == "T1":
        return random.choices(["Gold","Silver","Bronze",""], weights=[20,35,40,5])[0] or None
    elif tier == "T2":
        return random.choices(["Silver","Bronze",""], weights=[40,55,5])[0] or None
    else:
        return None

segments = [assign_segment(t) for t in tiers]

# CSM assignment — T3 mostly unassigned
def assign_csm(tier):
    if tier == "T1":   return f"CSM_{random.randint(1,40):04d}"
    elif tier == "T2": return f"CSM_{random.randint(41,70):04d}" if random.random() > 0.15 else None
    else:              return f"CSM_{random.randint(71,86):04d}" if random.random() > 0.60 else None

csm_ids = [assign_csm(t) for t in tiers]

dim_customers = pd.DataFrame({
    "customer_id":        customer_ids,
    "company_name":       [fake.company() for _ in range(N_CUSTOMERS)],
    "business_type":      np.random.choice(["SME","Enterprise","Startup","Freelancer","NGO"],
                                            N_CUSTOMERS, p=[0.55,0.15,0.20,0.08,0.02]),
    "industry_segment":   np.random.choice(INDUSTRY_SEGMENTS, N_CUSTOMERS),
    "city":               cities,
    "state":              states,
    "tier":               tiers,
    "acquisition_channel":np.random.choice(ACQUISITION_CHANNELS, N_CUSTOMERS,
                                            p=[0.25,0.20,0.15,0.15,0.10,0.07,0.05,0.03]),
    "account_manager_id": csm_ids,
    "onboarding_date":    onboarding_dates,
    "kyc_status":         np.random.choice(["VERIFIED","PENDING","REJECTED","EXPIRED"],
                                            N_CUSTOMERS, p=[0.91,0.05,0.02,0.02]),
    "segment_label":      segments,
    "is_active":          True,  # will update after subscriptions
    "created_at":         [
                            datetime.combine(d, datetime.min.time()) + timedelta(hours=random.randint(8,18))
                            for d in onboarding_dates
                          ],
    "updated_at":         [
                            datetime.combine(date(2026,3,31), datetime.min.time()) - timedelta(days=random.randint(0,90))
                            for _ in range(N_CUSTOMERS)
                          ],
})

# Introduce ~0.8% city/state mismatches (documented data quality issue)
n_mismatches = int(N_CUSTOMERS * 0.008)
mismatch_idx = np.random.choice(N_CUSTOMERS, n_mismatches, replace=False)
dim_customers.loc[mismatch_idx, "state"] = np.random.choice(
    ["Maharashtra","Karnataka","Tamil Nadu"], n_mismatches
)

dim_customers.to_csv(f"{OUTPUT_DIR}/dim_customers.csv", index=False)
print(f"  -> dim_customers: {len(dim_customers):,} rows")


print("Generating fact_subscriptions ...")
# ─────────────────────────────────────────────
# TABLE 2 — fact_subscriptions
# ─────────────────────────────────────────────
# Every customer has at least one subscription. Some churned and re-subscribed.
subs = []
sub_counter = 1

for i, row in dim_customers.iterrows():
    cid     = row["customer_id"]
    ob_date = row["onboarding_date"]

    # First subscription starts on onboarding date
    plan_choice  = random.choices(PLANS, weights=[15,10,30,20,15,10])[0]
    plan_type    = plan_choice[0]
    plan_mrr     = plan_choice[1] if "Monthly" in plan_choice[2] else round(plan_choice[1]/12, 2)
    contract     = plan_choice[2]

    sub_start = ob_date
    renewal_count = 0
    is_churned  = False
    churn_date  = None
    churn_reason = None
    sub_end     = None

    # Simulate lifecycle: churn probability per 30-day period
    current_date = sub_start
    while current_date < END_DATE:
        if random.random() < MONTHLY_CHURN:
            # Customer churns
            churn_date   = current_date + timedelta(days=random.randint(5, 28))
            churn_date   = min(churn_date, END_DATE)
            churn_reason = random.choice(CHURN_REASONS)
            sub_end      = churn_date
            is_churned   = True
            break
        renewal_count += 1
        current_date  += timedelta(days=30 if contract == "Monthly" else 365)

    last_renewal = sub_start + timedelta(days=30 * renewal_count) if renewal_count > 0 else None
    discount     = round(random.choice([0, 0, 0, 5, 10, 15, 20, 25]), 2)

    subs.append({
        "subscription_id":   f"SUB_{sub_counter:08d}",
        "customer_id":       cid,
        "plan_type":         plan_type,
        "plan_mrr":          plan_mrr,
        "subscription_start":sub_start,
        "subscription_end":  sub_end,
        "churn_date":        churn_date,
        "churn_reason":      churn_reason,
        "is_churned":        is_churned,
        "renewal_count":     renewal_count,
        "last_renewal_date": last_renewal,
        "discount_pct":      discount,
        "contract_type":     contract,
    })
    sub_counter += 1

    # ~15% of churned customers come back
    if is_churned and random.random() < 0.15 and churn_date and churn_date < END_DATE - timedelta(days=60):
        re_start     = churn_date + timedelta(days=random.randint(30, 90))
        new_plan     = random.choices(PLANS, weights=[15,10,30,20,15,10])[0]
        subs.append({
            "subscription_id":   f"SUB_{sub_counter:08d}",
            "customer_id":       cid,
            "plan_type":         new_plan[0],
            "plan_mrr":          new_plan[1] if "Monthly" in new_plan[2] else round(new_plan[1]/12,2),
            "subscription_start":re_start,
            "subscription_end":  None,
            "churn_date":        None,
            "churn_reason":      None,
            "is_churned":        False,
            "renewal_count":     random.randint(1,6),
            "last_renewal_date": re_start + timedelta(days=30),
            "discount_pct":      round(random.choice([0,10,15,20]),2),
            "contract_type":     new_plan[2],
        })
        sub_counter += 1

fact_subscriptions = pd.DataFrame(subs)

# Update is_active in dim_customers based on subscription status
churned_customers = set(
    fact_subscriptions[fact_subscriptions["is_churned"] == True]["customer_id"]
)
# Only mark inactive if they have no active sub
active_subs = set(
    fact_subscriptions[fact_subscriptions["is_churned"] == False]["customer_id"]
)
inactive_customers = churned_customers - active_subs
dim_customers.loc[dim_customers["customer_id"].isin(inactive_customers), "is_active"] = False

# Re-save dim_customers with corrected is_active
dim_customers.to_csv(f"{OUTPUT_DIR}/dim_customers.csv", index=False)

fact_subscriptions.to_csv(f"{OUTPUT_DIR}/fact_subscriptions.csv", index=False)
print(f"  -> fact_subscriptions: {len(fact_subscriptions):,} rows | Churned: {fact_subscriptions['is_churned'].sum():,}")


print("Generating fact_transactions ...")
# ─────────────────────────────────────────────
# TABLE 3 — fact_transactions
# ─────────────────────────────────────────────
transactions = []
txn_counter  = 1

# Fee rates by transaction type
fee_rates = {
    "UPI": 0.0025, "NEFT": 0.001, "IMPS": 0.0015,
    "Card_Debit": 0.009, "Card_Credit": 0.018,
    "BNPL": 0.022, "Wallet": 0.012, "RTGS": 0.0005
}

for i, row in dim_customers.iterrows():
    cid = row["customer_id"]
    ob  = row["onboarding_date"]

    # Get this customer's subscription period
    cust_subs = fact_subscriptions[fact_subscriptions["customer_id"] == cid]
    if cust_subs.empty:
        continue

    # Determine how active they are: higher-tier = more transactions
    tier = row["tier"]
    base_txns_per_month = {"T1": 30, "T2": 18, "T3": 8}.get(tier, 12)

    # Walk through each month they were subscribed
    for _, sub in cust_subs.iterrows():
        period_start = sub["subscription_start"]
        period_end   = sub["churn_date"] if sub["is_churned"] and sub["churn_date"] else END_DATE
        period_end   = min(period_end, END_DATE)

        current = period_start
        while current <= period_end:
            month_end = min(
                date(current.year, current.month, 28),
                period_end
            )
            # Volume declines in last 60 days before churn (behavioral signal)
            days_before_churn = (period_end - current).days if sub["is_churned"] else 999
            volume_factor     = 0.4 if days_before_churn < 60 else 1.0
            n_txns            = max(1, int(np.random.poisson(base_txns_per_month * volume_factor)))

            for _ in range(n_txns):
                day_range = max(0, (month_end - current).days)
                txn_date  = current + timedelta(days=random.randint(0, day_range) if day_range > 0 else 0)
                txn_type  = random.choices(TRANSACTION_TYPES, weights=[35,15,15,12,8,7,5,3])[0]
                # Amount varies by business type
                if row["business_type"] == "Enterprise":
                    amount = round(np.random.lognormal(11, 1.2), 2)
                elif row["business_type"] == "SME":
                    amount = round(np.random.lognormal(10, 1.0), 2)
                else:
                    amount = round(np.random.lognormal(9, 1.1), 2)
                amount = max(100.0, min(amount, 5_000_000.0))

                # Failure rate higher near churn
                fail_p  = 0.10 if days_before_churn < 30 else 0.035
                status  = random.choices(
                    ["SUCCESS","FAILED","PENDING","REFUNDED"],
                    weights=[1-fail_p-0.005-0.01, fail_p, 0.005, 0.01]
                )[0]

                fee        = round(amount * fee_rates.get(txn_type, 0.01), 4)
                fail_rsn   = random.choice(FAILURE_REASONS) if status == "FAILED" else None
                # Inject data quality issue: ~1.4% of FAILED have NULL failure_reason
                if status == "FAILED" and random.random() < 0.014:
                    fail_rsn = None

                transactions.append({
                    "transaction_id":     f"TXN_{txn_date.year}_{txn_counter:08d}",
                    "customer_id":        cid,
                    "transaction_date":   txn_date,
                    "transaction_amount": amount,
                    "transaction_type":   txn_type,
                    "payment_status":     status,
                    "merchant_category_code": random.choice(MCC_CODES),
                    "gateway_fee":        fee,
                    "failure_reason":     fail_rsn,
                    "product_used":       random.choice(["VelocityGateway","VelocityStack","Both"]),
                    "settlement_lag_days":random.choices([1,2,3,4,5],[60,25,8,4,3])[0],
                    "dim_date_id":        int(txn_date.strftime("%Y%m%d")),
                })
                txn_counter += 1

            # Next month
            if current.month == 12:
                current = date(current.year + 1, 1, 1)
            else:
                current = date(current.year, current.month + 1, 1)

    # Progress indicator every 1000 customers
    if (i + 1) % 1000 == 0:
        print(f"  Transactions: processed {i+1:,}/{N_CUSTOMERS:,} customers | {len(transactions):,} rows so far")

fact_transactions = pd.DataFrame(transactions)
fact_transactions.to_csv(f"{OUTPUT_DIR}/fact_transactions.csv", index=False)
print(f"  -> fact_transactions: {len(fact_transactions):,} rows")


print("Generating fact_product_usage ...")
# ─────────────────────────────────────────────
# TABLE 4 — fact_product_usage
# ─────────────────────────────────────────────
usage_rows   = []
usage_counter = 1

FEATURES  = ["POS_Analytics","Payment_Dashboard","Settlement_Reports",
             "API_Manager","Webhook_Config","Invoice_Generator",
             "Loyalty_Module","Staff_Management","Inventory_Sync",
             "Tax_Reports","BNPL_Portal","Support_Chat"]
N_FEATURES = len(FEATURES)

# Sample 60% of customers for usage data (not all use the platform API)
usage_customers = dim_customers.sample(frac=0.6, random_state=42)

for _, row in usage_customers.iterrows():
    cid  = row["customer_id"]
    ob   = row["onboarding_date"]

    # Get churn date if applicable
    cust_sub  = fact_subscriptions[fact_subscriptions["customer_id"] == cid].sort_values("subscription_start")
    if cust_sub.empty:
        continue
    last_sub   = cust_sub.iloc[-1]
    period_end = last_sub["churn_date"] if last_sub["is_churned"] and last_sub["churn_date"] else END_DATE
    period_end = min(period_end, END_DATE)

    # Generate ~2 usage snapshots per month per customer (weekly)
    current = ob
    while current <= period_end:
        days_before_churn = (period_end - current).days if last_sub["is_churned"] else 999

        # Usage drops before churn
        engagement_factor = max(0.1, 1 - (1 / max(days_before_churn, 1)) * 30) if days_before_churn < 90 else 1.0
        is_active_day     = random.random() < (0.75 * engagement_factor)

        api_calls   = max(0, int(np.random.poisson(500 * engagement_factor))) if is_active_day else 0
        failed_api  = int(api_calls * random.uniform(0.01, 0.05)) if api_calls > 0 else 0
        features    = random.randint(1, N_FEATURES) if is_active_day else 0
        session_min = round(random.uniform(5, 120) * engagement_factor, 2) if is_active_day else 0.0
        tickets     = random.choices([0,0,0,1,2,3], weights=[60,15,10,8,4,3])[0]
        nps         = random.randint(0,10) if random.random() < 0.12 else None  # 12% survey response
        last_login  = 1 if is_active_day else random.randint(2, max(3, min(days_before_churn + 1, 90)))

        usage_rows.append({
            "usage_id":             usage_counter,
            "customer_id":          cid,
            "event_date":           current,
            "dau_flag":             is_active_day,
            "api_calls_count":      api_calls,
            "failed_api_calls":     failed_api,
            "features_used_count":  features,
            "session_duration_mins":session_min,
            "support_tickets_raised":tickets,
            "nps_score":            nps,
            "last_login_days_ago":  last_login,
            "product_module":       random.choice(FEATURES) if is_active_day else None,
        })
        usage_counter += 1
        current += timedelta(days=random.randint(6, 10))  # roughly weekly snapshots

fact_product_usage = pd.DataFrame(usage_rows)
fact_product_usage.to_csv(f"{OUTPUT_DIR}/fact_product_usage.csv", index=False)
print(f"  -> fact_product_usage: {len(fact_product_usage):,} rows")


print("Generating fact_loan_accounts ...")
# ─────────────────────────────────────────────
# TABLE 5 — fact_loan_accounts
# ─────────────────────────────────────────────
loan_customers = dim_customers[dim_customers["kyc_status"] == "VERIFIED"].sample(
    frac=LOAN_COVERAGE, random_state=99
)

loans      = []
loan_counter = 1

for _, row in loan_customers.iterrows():
    cid = row["customer_id"]
    ob  = row["onboarding_date"]

    # Customers need at least 3 months of history before getting a loan
    earliest_loan = ob + timedelta(days=90)
    if earliest_loan >= END_DATE - timedelta(days=30):
        continue

    n_loans = random.choices([1,2,3],[0.65,0.25,0.10])[0]

    for k in range(n_loans):
        loan_type    = random.choice(LOAN_TYPES)
        loan_days_available = (END_DATE - earliest_loan - timedelta(days=30)).days
        if loan_days_available <= 0:
            continue
        disbursement = earliest_loan + timedelta(days=random.randint(0, loan_days_available))
        tenure       = random.choice([6, 9, 12, 18, 24, 36])
        maturity     = disbursement + timedelta(days=tenure * 30)

        # Loan amount varies by business type
        bt = row["business_type"]
        if bt == "Enterprise":
            amount = round(random.uniform(500_000, 5_000_000), -3)
        elif bt == "SME":
            amount = round(random.uniform(100_000, 1_000_000), -3)
        else:
            amount = round(random.uniform(25_000, 200_000), -3)

        disbursed = round(amount * random.uniform(0.92, 1.0), 2)
        rate      = round(random.uniform(14.5, 24.0), 2)

        # Repayment simulation
        elapsed_months  = max(0, (END_DATE - disbursement).days // 30)
        repaid_fraction = min(1.0, elapsed_months / tenure)
        outstanding     = round(disbursed * (1 - repaid_fraction), 2)

        # NPA logic: 3.1% overall NPA rate; higher for certain segments
        is_npa_segment = row["industry_segment"] in ["Construction_Real_Estate","Travel_Hospitality","Media_Entertainment"]
        npa_prob       = 0.08 if is_npa_segment else 0.025
        is_npa         = maturity < END_DATE and random.random() < npa_prob

        if is_npa:
            dpd        = random.randint(91, 540)
            status     = random.choice(["NPA","RESTRUCTURED"])
            npa_class  = random.choices(
                ["Sub-Standard","Doubtful","Loss"],
                weights=[50,30,20]
            )[0]
        elif maturity < END_DATE:
            dpd       = 0
            status    = "CLOSED"
            npa_class = None
            outstanding = 0.0
        else:
            dpd       = random.choices([0,0,0,0,1,5,15,30,45,60],[50,15,10,8,6,4,3,2,1,1])[0]
            status    = "ACTIVE"
            npa_class = None

        credit_score = random.randint(580, 800)

        loans.append({
            "loan_id":                  f"LN_{disbursement.year}_{loan_counter:08d}",
            "customer_id":              cid,
            "loan_type":                loan_type,
            "loan_amount":              amount,
            "disbursed_amount":         disbursed,
            "interest_rate_pct":        rate,
            "tenure_months":            tenure,
            "disbursement_date":        disbursement,
            "maturity_date":            maturity,
            "outstanding_principal":    outstanding,
            "dpd_days":                 dpd,
            "npa_flag":                 is_npa,
            "npa_classification":       npa_class,
            "credit_score_at_origination": credit_score,
            "loan_status":              status,
        })
        loan_counter += 1
        earliest_loan = maturity + timedelta(days=90)  # gap before next loan

fact_loan_accounts = pd.DataFrame(loans)
fact_loan_accounts.to_csv(f"{OUTPUT_DIR}/fact_loan_accounts.csv", index=False)
print(f"  -> fact_loan_accounts: {len(fact_loan_accounts):,} rows | NPA: {fact_loan_accounts['npa_flag'].sum()}")


# ─────────────────────────────────────────────
# REFERENTIAL INTEGRITY CHECK
# ─────────────────────────────────────────────
print("\nRunning referential integrity checks ...")

all_cust_ids = set(dim_customers["customer_id"])

def check_fk(table, name, col):
    orphans = set(table[col]) - all_cust_ids
    status  = "PASS" if len(orphans) == 0 else f"FAIL — {len(orphans)} orphan IDs"
    print(f"  {name}.{col} -> dim_customers.customer_id : {status}")

check_fk(fact_transactions,  "fact_transactions",  "customer_id")
check_fk(fact_subscriptions, "fact_subscriptions", "customer_id")
check_fk(fact_product_usage, "fact_product_usage", "customer_id")
check_fk(fact_loan_accounts, "fact_loan_accounts", "customer_id")


# ─────────────────────────────────────────────
# SUMMARY STATS
# ─────────────────────────────────────────────
print("\n" + "="*55)
print("GENERATION COMPLETE — Summary Statistics")
print("="*55)
print(f"dim_customers       : {len(dim_customers):>10,} rows")
print(f"fact_subscriptions  : {len(fact_subscriptions):>10,} rows")
print(f"fact_transactions   : {len(fact_transactions):>10,} rows")
print(f"fact_product_usage  : {len(fact_product_usage):>10,} rows")
print(f"fact_loan_accounts  : {len(fact_loan_accounts):>10,} rows")
print("-"*55)
print(f"Churn rate (subs)   : {fact_subscriptions['is_churned'].mean()*100:.1f}%")
print(f"NPA rate (loans)    : {fact_loan_accounts['npa_flag'].mean()*100:.1f}%")
print(f"Txn success rate    : {(fact_transactions['payment_status']=='SUCCESS').mean()*100:.1f}%")
print(f"Output directory    : {OUTPUT_DIR}/")
print("="*55)
