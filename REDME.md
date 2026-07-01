# 🚀 VelocityPay Analytics Platform

> End-to-End Data Analytics, Machine Learning & Power BI Project for a FinTech Company

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black)

---

# 📌 Project Overview

VelocityPay Analytics Platform is an end-to-end Data Analytics project developed for a fictional FinTech company that provides digital payment solutions, subscription services, SME lending, and product engagement platforms.

The project demonstrates the complete analytics lifecycle, beginning with raw business data and progressing through exploratory analysis, business KPI development, customer segmentation, machine learning, and interactive Power BI dashboards.

This project simulates a real-world enterprise analytics workflow similar to what a Data Analyst or Business Intelligence Developer would build in a production environment.

---

# 🎯 Business Problem

VelocityPay's management team needs a centralized analytics solution to answer key business questions such as:

- How much revenue is generated every month?
- Which industries contribute the highest revenue?
- Why are customers churning?
- Which customers are at the highest risk of churn?
- Which customers are the most valuable?
- How healthy is the loan portfolio?
- Which products have the highest customer engagement?
- Which KPIs should executives monitor daily?

To address these challenges, an integrated analytics platform was developed using Python, SQL, Machine Learning, and Power BI.

---

# 🎯 Project Objectives

The project focuses on solving the following business objectives:

- Analyze customer transaction behavior
- Monitor payment success rate
- Detect revenue leakage
- Analyze customer churn
- Identify churn reasons
- Measure churn revenue impact
- Perform customer segmentation using RFM analysis
- Predict customer churn using Machine Learning
- Explain important prediction factors
- Develop executive-level Power BI dashboards
- Generate business recommendations for management

---

# 📊 Dataset Summary

The project is based on synthetic business data representing one year of operations.

| Dataset | Records |
|----------|---------:|
| Customers | 10,000 |
| Transactions | 3,178,051 |
| Subscriptions | 10,674 |
| Loan Accounts | 3,915 |
| Product Usage Events | 375,118 |

---

# 🏗 Project Architecture

```

CSV Data

↓

Python Analysis

↓

EDA

↓

SQL Analytics

↓

Business KPI Analysis

↓

Revenue Leakage Analysis

↓

Customer Churn Analysis

↓

RFM Segmentation

↓

Machine Learning Dataset

↓

Random Forest Model

↓

Feature Importance Analysis

↓

Power BI Data Model

↓

Interactive Dashboards
# 🛠 Technology Stack

## Programming Language

- Python 3.11

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn
- Random Forest Classifier

## Explainable AI

- SHAP

## Business Intelligence

- Microsoft Power BI

## Database

- SQL

## Development Environment

- Visual Studio Code

## Version Control

- Git
- GitHub

---

# 📁 Project Structure

```

VelocityPay_Analytics_Platform/

│

├── dashboards/
│ └── VelocityPay_Analytics.pbix
│
├── data/
│ ├── dim_customers.csv
│ ├── fact_transactions.csv
│ ├── fact_subscriptions.csv
│ ├── fact_loan_accounts.csv
│ └── fact_product_usage.csv
│
├── docs/
│ ├── Project_Documentation.md
│ ├── Dashboard_Guide.md
│ ├── Business_Insights.md
│ ├── Data_Dictionary.md
│ ├── Installation_Guide.md
│ └── Technical_Architecture.md
│
├── reports/
│ ├── ml_dataset.csv
│ └── rfm_customers.csv
│
├── scripts/
│ ├── analysis_01.py
│ ├── analysis_02.py
│ ├── analysis_03.py
│ ├── analysis_04.py
│ ├── analysis_05_churn.py
│ ├── analysis_06_churn_reason.py
│ ├── analysis_07_churn_by_industry.py
│ ├── analysis_08_churn_rate_by_industry.py
│ ├── analysis_09_churn_revenue_impact.py
│ ├── rfm_analysis.py
│ ├── ml_dataset_builder.py
│ ├── random_forest_churn.py
│ ├── feature_importance.py
│ └── shap_analysis.py
│
├── sql/
│ └── velocitypay_schema.sql
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

```

---

# 🔄 Analytics Workflow

The project follows a structured analytics workflow commonly used in enterprise data analytics projects.

### Step 1 — Data Collection

Business data is collected from multiple operational datasets:

- Customer Information
- Transaction Records
- Subscription Data
- Loan Portfolio
- Product Usage

↓

### Step 2 — Data Processing

Python scripts perform:

- Data loading
- Cleaning
- Validation
- Aggregation
- KPI calculations

↓

### Step 3 — Exploratory Data Analysis

Business metrics analyzed include:

- Customer Distribution
- Industry Distribution
- Monthly Revenue
- Payment Status
- Revenue Leakage

↓

### Step 4 — Customer Churn Analysis

Performed analyses include:

- Overall Churn Rate
- Churn by Industry
- Churn Reasons
- Revenue Impact of Churn

↓

### Step 5 — RFM Customer Segmentation

Customers are segmented using:

- Recency
- Frequency
- Monetary Value

Generated customer segments:

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Others

↓

### Step 6 — Machine Learning

Machine Learning pipeline:

- Feature Engineering
- Dataset Preparation
- Random Forest Classification
- Churn Prediction
- Feature Importance Analysis

↓

### Step 7 — Business Intelligence

Processed data is visualized through interactive Power BI dashboards for executive decision-making.

---

# 📈 Business KPIs

The following KPIs are tracked across the dashboards:

### Customer KPIs

- Total Customers
- Active Customers
- Customer Segments
- Customer Churn Rate

---

### Revenue KPIs

- Total Revenue
- Monthly Revenue
- Revenue by Industry
- Revenue Leakage

---

### Transaction KPIs

- Total Transactions
- Success Rate
- Failed Transactions
- Pending Transactions
- Refunded Transactions

---

### Loan KPIs

- Total Loans
- Approved Loans
- Rejected Loans
- Approval Rate
- Loan Amount

---

### Product Usage KPIs

- Total Usage Events
- Active Users
- Average Session Duration
- Feature Adoption

---

### Machine Learning KPIs

- Model Accuracy
- Customer Churn Prediction
- Feature Importance
- High-Risk Customers

---# 📊 Power BI Dashboards

The project includes seven interactive dashboards that provide business insights across different functional areas.

---

## 1. Executive Dashboard

The Executive Dashboard provides a high-level summary of business performance.

### KPIs

- Total Revenue
- Total Customers
- Total Transactions
- Payment Success Rate
- Customer Churn Rate

### Visuals

- Monthly Revenue Trend
- Revenue by Industry
- Transaction Status Distribution

### Business Value

Provides executives with a centralized view of company performance and supports strategic decision-making.

---

## 2. Customer & Revenue Dashboard

This dashboard focuses on customer behavior and revenue generation.

### KPIs

- Total Revenue
- Total Customers
- Average Revenue per Customer

### Visuals

- Revenue by Industry
- Monthly Revenue Trend
- Customer Distribution
- Industry Distribution

### Business Value

Helps identify high-value customer segments and revenue-generating industries.

---

## 3. Customer Churn Dashboard

This dashboard analyzes customer attrition and its business impact.

### KPIs

- Total Customers
- Churned Customers
- Churn Rate
- Monthly
### KPIs

- Total Customers
- Churned Customers
- Churn Rate
- Monthly Revenue Lost

### Visuals

- Churn by Industry
- Churn Reasons
- Churn Rate by Industry
- Revenue Impact of Churn

### Business Value

Helps identify customer retention opportunities and prioritize actions to reduce churn.

---

## 4. RFM Segmentation Dashboard

This dashboard classifies customers based on purchasing behavior.

### KPIs

- Average Recency
- Average Frequency
- Average Monetary Value

### Customer Segments

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Others

### Business Value

Supports customer retention strategies, personalized marketing campaigns, and loyalty programs.

---

## 5. Loan Analytics Dashboard

This dashboard provides insights into the company's lending portfolio.

### KPIs

- Total Loans
- Approved Loans
- Rejected Loans
- Approval Rate

### Visuals

- Loan Status Distribution
- Loan Amount by Industry
- Loan Applications by State
- Loan Status by Industry

### Business Value

Enables loan managers to monitor portfolio performance and identify lending trends.

---

## 6. Product Usage Dashboard

This dashboard analyzes customer engagement with company products.

### KPIs

- Total Usage Events
- Active Customers
- Average Session Duration
- Product Adoption Rate

### Visuals

- Usage by Product
- Usage by Industry
- Top Active Customers
- Monthly Usage Trend

### Business Value

Helps product managers understand customer engagement and identify opportunities to improve product adoption.

---

## 7. Machine Learning Dashboard

This dashboard summarizes the output of the churn prediction model.

### KPIs

- Model Accuracy
- Predicted Churn Customers
- High-Risk Customers

### Visuals

- Feature Importance
- Prediction Distribution
- Customer Risk Categories

### Business Value

Supports proactive customer retention by identifying customers at high risk of churn.

---

# 📌 Key Business Insights

The project identified several important business findings:

- Payment success rate is approximately **94.93%**, indicating a stable payment infrastructure.
- Failed transactions still contribute to significant potential revenue leakage.
- Customer churn remains a major business challenge, with an observed churn rate of approximately **44.58%**.
- Revenue contribution varies across industry segments.
- RFM segmentation identifies high-value customers and customers requiring retention efforts.
- The Random Forest model achieved approximately **94% accuracy** in churn prediction.
- Feature importance analysis highlights customer activity metrics as the strongest predictors of churn.

---

# 💡 Business Recommendations

Based on the analysis, the following recommendations are proposed:

- Improve payment gateway reliability to reduce failed transactions.
- Strengthen customer retention programs for high-risk customer segments.
- Enhance customer support to address common churn reasons.
- Focus marketing efforts on high-revenue industries.
- Expand loyalty programs for Champions and Loyal Customers.
- Continuously monitor loan portfolio performance.
- Use machine learning predictions to trigger proactive retention campaigns.

---

# 🚀 Future Enhancements

Potential improvements for future versions include:

- Real-time data pipelines
- Cloud-based data warehouse integration
- Power BI Service deployment
- Automated ETL workflows
- Customer Lifetime Value (CLV) prediction
- Recommendation engine
- MLOps pipeline for automated model retraining
- REST API integration
- Role-based dashboard security

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/VelocityPay-Analytics-Platform.git
```

Navigate to the project:

```bash
cd VelocityPay-Analytics-Platform
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📂 Documentation

Additional documentation is available in the `docs` folder:

- Project_Documentation.md
- Technical_Architecture.md
- Dashboard_Guide.md
- Business_Insights.md
- Data_Dictionary.md
- Installation_Guide.md

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sakshiba Jadeja**

Aspiring Data Analyst | Power BI Developer | Python | SQL | Machine Learning

GitHub: https://github.com/<your-username>

LinkedIn: https://www.linkedin.com/in/<your-linkedin-profile>

---

# ⭐ Acknowledgements

This project was developed as a portfolio project to demonstrate end-to-end Data Analytics skills, including:

- Data Processing
- Business Analysis
- SQL
- Python
- Machine Learning
- Power BI Dashboard Development
- Business Documentation
- GitHub Project Management

The project simulates real-world business scenarios commonly encountered in the FinTech industry.
