-- Query for Glam rock band
SELECT band_name,
(IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

