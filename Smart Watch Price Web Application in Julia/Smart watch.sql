/* ANALYZE THE SMART WATCH DATA BY ANSWERING THE QUESTIONS AS FOLLOWS */

/* View entire table */
SELECT * FROM Cleanedsmartwatchprices;

/* What top 5 brands has the highest price? */
SELECT brand, price_usd FROM Cleanedsmartwatchprices
ORDER BY price_usd DESC
LIMIT 5;

/* What is the most commonly used os by smart watches? */
SELECT operating_system, COUNT(*) AS Occurence FROM Cleanedsmartwatchprices
GROUP BY operating_system 
ORDER BY Occurence DESC
LIMIT 10;

/* What connectivity medium do most of the smart watches use? */
SELECT connectivity, COUNT(*) AS Occurence FROM Cleanedsmartwatchprices
GROUP BY connectivity 
ORDER BY Occurence DESC
LIMIT 5;

/* What top 5 brands has the longest battery life in days? */
SELECT DISTINCT brand, battery_life_days FROM Cleanedsmartwatchprices
ORDER BY battery_life_days DESC
LIMIT 7;

/* What percentage of smart watch have and have not GPS? */
WITH derived_gps AS (
    SELECT 
        gps, 
        CASE 
            WHEN gps = 'Yes' THEN 1 
            ELSE 0 
        END AS new_gps 
    FROM 
        Cleanedsmartwatchprices
)
SELECT 
    gps, new_gps, 
    COUNT(*) AS OCCURENCE,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER()) AS percentage
FROM 
    derived_gps 
GROUP BY 
    new_gps;
    
/* What percentage of smart watch have and have not NFC? */
WITH derived_nfc AS (
    SELECT 
        nfc, 
        CASE 
            WHEN nfc = 'Yes' THEN 1 
            ELSE 0 
        END AS new_nfc 
    FROM 
        Cleanedsmartwatchprices
)
SELECT 
    nfc, new_nfc, 
    COUNT(*) AS occurence,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER()) AS percentage
FROM 
    derived_nfc 
GROUP BY 
    new_nfc;