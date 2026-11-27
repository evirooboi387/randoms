# Movies Analytics using Azure Data Factory

## Project Overview

An end-to-end ETL pipeline using Azure Data Factory to
process movie and rating datasets and store aggregated
genre counts in Azure SQL Database.

## Technologies Used

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure SQL Database
- Mapping Data Flow
- SQL

## Project Workflow

1. Upload movies.csv and ratings.csv to ADLS Gen2.
2. Copy the source files into the staging directory.
3. Filter movies with ratings greater than 2.
4. Remove duplicate movie IDs.
5. Join movies and ratings datasets.
6. Split and flatten movie genres.
7. Aggregate genre occurrences.
8. Load the results into Azure SQL Database.

## Results

- Successfully executed the ETL pipeline.
- Generated 20 unique genre records.
- Stored the results in test.generes.
- Performed SQL data validation.

## Documentation

The Word document contains implementation steps,
screenshots, pipeline execution and final SQL results.
