-- Create schema
CREATE SCHEMA test;
GO

-- Create destination table
CREATE TABLE test.generes (
    genre VARCHAR(100) NOT NULL,
    [count] BIGINT NOT NULL
);
GO

-- Display final results
SELECT *
FROM test.generes
ORDER BY [count] DESC;

-- Count unique genres
SELECT COUNT(*) AS total_unique_genres
FROM test.generes;

-- Check duplicate genres
SELECT genre, COUNT(*) AS occurrences
FROM test.generes
GROUP BY genre
HAVING COUNT(*) > 1;

-- Check invalid records
SELECT *
FROM test.generes
WHERE genre IS NULL
   OR [count] <= 0;
