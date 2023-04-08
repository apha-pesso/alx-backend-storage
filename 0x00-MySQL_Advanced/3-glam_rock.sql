-- Query for Glam rock band
-- (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
-- (split - formed) AS lifespan
SELECT band_name,
(CASE WHEN split IS NOT NULL THEN (split - formed) ELSE (2023 - formed) END) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

