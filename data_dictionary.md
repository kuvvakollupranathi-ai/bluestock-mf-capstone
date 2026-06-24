# Mutual Fund Analytics Data Dictionary

## dim_fund
| Column | Type | Description |
|----------|---------|---------|
| fund_id | INTEGER | Primary Key |
| amfi_code | INTEGER | AMFI Fund Code |
| scheme_name | TEXT | Mutual Fund Scheme |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund Category |

## dim_date
| Column | Type | Description |
|----------|---------|---------|
| date_id | INTEGER | Primary Key |
| full_date | DATE | Calendar Date |
| year | INTEGER | Year |
| month | INTEGER | Month |
| quarter | INTEGER | Quarter |

## fact_nav
| Column | Type | Description |
|----------|---------|---------|
| nav_id | INTEGER | Primary Key |
| fund_id | INTEGER | Fund Reference |
| date_id | INTEGER | Date Reference |
| nav | REAL | Net Asset Value |

## fact_transactions
| Column | Type | Description |
|----------|---------|---------|
| transaction_id | INTEGER | Primary Key |
| investor_id | TEXT | Investor Identifier |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |