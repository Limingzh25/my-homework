# CSE 583 Homework 1: Bicycle Data Analysis

## Overview

This project analyzes hourly bicycle counts on Seattle's Fremont Bridge using Python, pandas, and matplotlib. The analysis focuses on data collected in 2016.

## Dataset

The dataset was obtained from Seattle Open Data and contains hourly bicycle counts on the east and west sidewalks of the Fremont Bridge.

The original dataset contains four columns: Date, Total, Cyclist West Sidewalk, and Cyclist East Sidewalk.

## Data Analysis Process

1. **Loading Data:** I used `pd.read_csv()` to import the CSV file into a pandas DataFrame.

2. **Data Types:** I inspected the data types and converted the Date column to datetime format using `pd.to_datetime()`. Bicycle counts were stored as numeric values.

3. **New Variables:** I created three columns:
   - `Total`: Sum of East and West bicycle counts.
   - `Hour`: Hour of the day (0–23).
   - `Year`: Calendar year.

4. **Filtering:** I selected observations from 2016 using pandas.

5. **Missing Data:** The 2016 dataset contained 8,784 observations, with one observation containing missing bicycle counts. I removed this observation, leaving 8,783 complete records for analysis.

6. **Visualization:** I grouped the observations by hour and calculated the average bicycle count for each hour. I used matplotlib to create a line plot and saved it as `counts_by_hour.png`.

7. **Busiest Hour:** I used `idxmax()` to identify the hour with the highest average bicycle count.

## Results

The busiest hour in 2016 was **17:00 (5 PM)**, with an average bicycle count of approximately **399.03**.

The data also show two prominent peaks around 8 AM and 5 PM, suggesting that bicycle traffic is particularly high during commuting hours.

## Datetime Formats

Python's `datetime.datetime` represents individual dates and times. NumPy's `datetime64` is designed for efficient storage and operations on arrays of timestamps. Pandas provides datetime functionality for Series and DataFrames, including the `.dt` accessor for extracting components such as hours and years.

In this analysis, I used pandas datetime functionality to extract the hour and year from the Date column.

## AI Assistance

I used ChatGPT to help understand pandas functions, Python syntax, data cleaning, and visualization. I reviewed the suggested code and ran the analysis to verify the results.

## How to Run

Install the required dependencies listed in `pyproject.toml`, download the CSV dataset into `src/hw1_data_analysis/bicycle_data.csv`, and run:

```bash
python src/hw1_data_analysis/hw1.py
```

The script generates `counts_by_hour.png`.

## Data Source

Seattle Open Data: Fremont Bridge Bicycle Counts

https://data.seattle.gov/d/65db-xm6k
