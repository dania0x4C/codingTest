SELECT COUNT(*) as FISH_COUNT, MAX(LENGTH) as MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE ASC