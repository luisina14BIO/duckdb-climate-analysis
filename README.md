# Meteorological Data Analysis with DuckDB

An analytical project using **DuckDB and SQL** to explore daily temperature records from Central Park, New York, using a CSV file as the data source.

The project demonstrates how to perform analytical queries directly on files without creating a persistent database.

## Project Objectives

* Query CSV data directly with DuckDB.
* Calculate descriptive statistics and temperature aggregates.
* Compare temperature patterns by year and month.
* Identify days with the largest daily temperature ranges.
* Apply basic data quality checks and document query execution times.

## Dataset

* **Source:** NOAA — Global Historical Climatology Network Daily (GHCN-Daily).
* **Station:** Central Park, New York (`USW00094728`).
* **Period available in the processed dataset:** January 1, 2021 – February 5, 2025.
* **Records:** 1,497 daily observations.
* **Variables:** station ID, date, maximum temperature (°C), and minimum temperature (°C).

Data source: [NOAA GHCN-Daily — Central Park station](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00094728.csv).

Temperatures are converted from tenths of degrees Celsius to degrees Celsius during data preparation. The processed dataset contains one record per date with both maximum and minimum temperatures available.

**Coverage note:** 2025 contains only 36 observations, from January 1 to February 5. Therefore, its annual averages should not be compared directly with full-year averages.

## Project Structure

```text
duckdb-climate-analysis/
├── data/
│   └── climate_data.csv
├── 01_data_extraction.ipynb
├── analysis.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies

* Python
* DuckDB
* SQL
* Pandas
* Jupyter Notebook

## Setup and Execution

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/duckdb-climate-analysis.git
cd duckdb-climate-analysis
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

```bash
python analysis.py
```

The script reads `data/climate_data.csv`, creates a temporary DuckDB view, filters records with missing temperatures, and executes the analytical queries.

No persistent DuckDB database file is created.

## Analytical Queries

The script includes the following analyses:

1. **Overall summary:** number of records, average maximum and minimum temperatures, and historical temperature extremes.
2. **Annual comparison:** yearly observation counts and average temperatures.
3. **Daily temperature range:** the ten dates with the largest difference between maximum and minimum temperatures.
4. **Monthly averages:** average maximum and minimum temperatures grouped by calendar month.
5. **Temporal coverage:** first and last available dates and observation counts for each year.

These queries demonstrate aggregations, grouping, sorting, derived metrics, and data quality validation using SQL.

## Key Findings

* **1,497 observations** are available in the processed dataset.
* Average daily maximum temperature: **17.62 °C**.
* Average daily minimum temperature: **9.87 °C**.
* Highest recorded daily maximum: **36.7 °C**.
* Lowest recorded daily minimum: **−16.0 °C**.
* July has the highest average daily maximum temperature among the calendar months in this dataset.
* The largest observed daily temperature range is **27.6 °C**, on December 23, 2022.

The results describe the available observations and should not be interpreted as a complete climate assessment.

## Query Execution Times

Observed execution times in the development environment:

| Query                   | Time (seconds) |
| ----------------------- | -------------: |
| Overall summary         |         0.2839 |
| Annual comparison       |         0.3490 |
| Daily temperature range |         0.1767 |
| Monthly averages        |         0.2704 |

These measurements include query execution and conversion of the results to Pandas DataFrames. Execution times may vary by machine and environment.

## Database Design Approach

DuckDB is used as an embedded analytical SQL engine. The CSV is accessed directly, and the temporary view exists only during script execution.

This approach avoids maintaining a separate database file while allowing SQL-based analysis of structured data.

## Future Improvements

* Extend the dataset to include a complete year for 2025.
* Visualize seasonal and annual temperature patterns.
* Compare temperature trends across multiple weather stations.
