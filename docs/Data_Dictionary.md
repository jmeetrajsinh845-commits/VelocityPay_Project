# Data Dictionary

# Overview

This document describes all datasets, important fields, data types, primary keys, foreign keys, and business definitions used in the VelocityPay Analytics Platform.

The purpose of this document is to help analysts, developers, and business users understand the project data model.

---

# Data Model

The project contains five primary business datasets.

1. Customer Master
2. Transaction History
3. Subscription Details
4. Loan Accounts
5. Product Usage

Additional analytical datasets:

- RFM Customer Table
- Machine Learning Dataset

---

# 1. Customer Master

Dataset Name

dim_customers

Description

Contains customer profile information.

Primary Key

customer_id

| Column | Data Type | Description |
|----------|-----------|-------------|
| customer_id | String | Unique customer identifier |
| company_name | String | Registered company name |
| industry_segment | String | Industry category |
| business_type | String | Business classification |
| city | String | Customer city |
| state | String | Customer state |
| onboarding_date | Date | Customer registration date |

---

# Business Purpose

Used for:

- Customer Analytics
- Industry Analysis
- Geographic
