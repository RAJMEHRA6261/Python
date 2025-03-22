CREATE DATABASE stock_analysis;
USE stock_analysis;

CREATE TABLE week_high_stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20),
    series VARCHAR(10),
    ltp DECIMAL(10, 2),
    pct_change DECIMAL(6, 2),
    new_52wh_price DECIMAL(10, 2),
    prev_high DECIMAL(10, 2),
    prev_high_date DATE
);

CREATE TABLE week_low_stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20),
    series VARCHAR(10),
    ltp DECIMAL(10, 2),
    pct_change DECIMAL(6, 2),
    new_52wl_price DECIMAL(10, 2),
    prev_low DECIMAL(10, 2),
    prev_low_date DATE
);

Select * from week_high_stocks;
Select * from week_low_stocks;

#1 Stocks hitting 52-week highs by Series
SELECT series, COUNT(*) AS high_count
FROM week_high_stocks
GROUP BY series
ORDER BY high_count DESC;

#2️ Stocks hitting 52-week lows by Series
SELECT series, COUNT(*) AS low_count
FROM week_low_stocks
GROUP BY series
ORDER BY low_count DESC;

#3️ Top 10 gainers (52-week highs) by % change
SELECT DISTINCT symbol, series, pct_change, ltp
FROM week_high_stocks
ORDER BY pct_change DESC
LIMIT 10;

#4️ Top 10 losers (52-week lows) by % change
SELECT DISTINCT symbol, series, pct_change, ltp
FROM week_low_stocks
ORDER BY pct_change ASC
LIMIT 10;

# Find common stocks that hit both 52 Week High & 52 Week Low in the year (high volatility stocks)
SELECT DISTINCT h.symbol 
FROM week_high_stocks h
INNER JOIN week_low_stocks l 
ON h.symbol = l.symbol;

#Compare the average % change of High stocks vs Low stocks
SELECT 
    'High' AS category, 
    AVG(h.pct_change) AS avg_pct_change
FROM week_high_stocks h

UNION ALL

SELECT 
    'Low' AS category, 
    AVG(l.pct_change) AS avg_pct_change
FROM week_low_stocks l;

DESCRIBE week_high_stocks;
DESCRIBE week_low_stocks;

#List top 5 strongest (near highs) and weakest (near lows) stocks
-- Stocks closest to their 52 Week High
SELECT DISTINCT symbol, ltp, new_52wh_price,
       ROUND(((ltp - new_52wh_price)/new_52wh_price) * 100, 2) AS pct_below_high
FROM week_high_stocks
ORDER BY pct_below_high ASC
LIMIT 5;

-- Stocks closest to their 52 Week Low
SELECT DISTINCT symbol, ltp, new_52wl_price,
       ROUND(((ltp - new_52wl_price)/new_52wl_price) * 100, 2) AS pct_above_low
FROM week_low_stocks
ORDER BY pct_above_low DESC
LIMIT 5;

-- For 52W High dataset
SELECT series, 
       COUNT(*) AS near_high_count,
       ROUND(AVG(((ltp - new_52wh_price) / new_52wh_price) * 100), 2) AS avg_pct_below_high
FROM week_high_stocks
GROUP BY series
ORDER BY near_high_count DESC;

-- For 52W Low dataset
SELECT series, 
       COUNT(*) AS near_low_count,
       ROUND(AVG(((ltp - new_52wl_price) / new_52wl_price) * 100), 2) AS avg_pct_above_low
FROM week_low_stocks
GROUP BY series
ORDER BY near_low_count DESC;














 
 
 

