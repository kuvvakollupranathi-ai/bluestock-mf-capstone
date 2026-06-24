-- 1 Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM 03_aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV per month
SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM 02_nav_history
GROUP BY month;

-- 3 SIP YoY Growth
SELECT *
FROM 04_monthly_sip_inflows
ORDER BY month;

-- 4 Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM 08_investor_transactions
GROUP BY state;

-- 5 Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio
FROM 07_scheme_performance
WHERE expense_ratio < 1;

-- 6 Top 10 Performing Schemes
SELECT scheme_name, return_1y
FROM 07_scheme_performance
ORDER BY return_1y DESC
LIMIT 10;

-- 7 Average Transaction Amount
SELECT AVG(amount_inr)
FROM 08_investor_transactions;

-- 8 Transaction Count by Type
SELECT transaction_type,
COUNT(*)
FROM 08_investor_transactions
GROUP BY transaction_type;

-- 9 Top Portfolio Holdings
SELECT *
FROM 09_portfolio_holdings
ORDER BY holding_percent DESC
LIMIT 10;

-- 10 Benchmark Index Summary
SELECT *
FROM 10_benchmark_indices;