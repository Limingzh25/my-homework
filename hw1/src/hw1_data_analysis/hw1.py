# Fremont Bridge Bicycle Data Analysis

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# --------------------Part 1: Read CSV into a pandas DataFrame--------------

data_path = Path(__file__).with_name("bicycle_data.csv")

df = pd.read_csv(data_path)

print("Original data:")
print(df.head())

print("\nOriginal data types:")
print(df.dtypes)


# ------------------------Part 2: Describe columns and update data types-----------------

# Date: date and time of observation; should be datetime
# East: bicycle count on east sidewalk; numeric (float)
# West: bicycle count on west sidewalk; numeric (float)
# Total: combined bicycle count; numeric (float)
# Hour: hour of the day (0-23); integer
# Year: calendar year; integer

# Rename the original columns for convenience
df = df.rename(columns={
    "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk": "East",
    "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk": "West"
})

# Keep Date, East, and West.
# We will calculate Total ourselves in Part 3.
df = df[["Date", "East", "West"]].copy()

# Convert Date to datetime
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%m/%d/%Y %I:%M:%S %p",
    errors="coerce"
)

# Ensure bicycle counts are numeric
df["East"] = pd.to_numeric(df["East"], errors="coerce")
df["West"] = pd.to_numeric(df["West"], errors="coerce")

print("\nUpdated data types:")
print(df.dtypes)


# --------------------Part 3: Add Total, Hour, and Year columns---------------------

# Total bicycle count
df["Total"] = df["East"] + df["West"]

# Hour of the day
df["Hour"] = df["Date"].dt.hour

# Year
df["Year"] = df["Date"].dt.year

print("\nData after adding new columns:")
print(df.head())

print("\nFinal column types:")
print(df.dtypes)

# ----------------Part 4: Create a subset for the year 2016-------------

df_2016 = df[df["Year"] == 2016].copy()

print("\nNumber of observations in 2016:")
print(len(df_2016))

print("\nFirst five observations in 2016:")
print(df_2016.head())


# ----------------Part 5: Check and handle missing data----------------

# Count rows with missing values
missing_count = df_2016[
    ["Date", "East", "West", "Total"]
].isna().any(axis=1).sum()

print("\nNumber of rows with missing values:")
print(missing_count)

# Show missing values in each column
print("\nMissing values by column:")
print(df_2016.isna().sum())

# Remove rows with missing data
df_2016 = df_2016.dropna(
    subset=["Date", "East", "West", "Total"]
).copy()

print("\nNumber of observations after removing missing data:")
print(len(df_2016))

# There is 1 observation with missing data in 2016.
# Both East and West counts are missing in this observation.
# The incomplete observation was removed before analysis.
# The remaining dataset contains 8783 observations.

# --------------------------------------------------
# Part 6: Plot average bicycle counts by hour
# --------------------------------------------------

# Calculate average bicycle counts for each hour
hourly_avg = df_2016.groupby("Hour")["Total"].mean()

print("\nAverage bicycle counts by hour:")
print(hourly_avg)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(
    hourly_avg.index,
    hourly_avg.values,
    marker="o"
)

plt.xlabel("Hour of the Day")
plt.ylabel("Average Bicycle Count")
plt.title("Average Hourly Bicycle Counts on Fremont Bridge (2016)")

plt.xticks(range(24))
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the figure
plt.savefig("counts_by_hour.png", dpi=300)
plt.close()

print("\nFigure saved as counts_by_hour.png")

# Part 7: Find the busiest hour of the day
# --------------------------------------------------

busiest_hour = hourly_avg.idxmax()
busiest_count = hourly_avg.max()

print("\nBusiest hour of the day:", busiest_hour)
print("Average bicycle count:", round(busiest_count, 2))

# The busiest hour in 2016 was 17:00 (5 PM).
# The average bicycle count during this hour was 399.03.

