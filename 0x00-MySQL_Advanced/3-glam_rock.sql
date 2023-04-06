-- Query for Glam rock band
-- (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
SELECT band_name,
(split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

