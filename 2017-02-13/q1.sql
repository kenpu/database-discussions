WITH RECURSIVE T(n) AS (
    SELECT 1 as n
    UNION
    SELECT (n+1) % 3 FROM T
) SELECT * FROM T;
