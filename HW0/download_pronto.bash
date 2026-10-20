#!/usr/bin/env bash
set -euo pipefail

# Run inside the folder containing this script (HW0).
cd "$(dirname "$0")"

# Create the Pronto project and data directories.
mkdir -p pronto/data

# Document the dataset.
echo "Pronto bike-share trip, station, weather, and status data for Seattle (2014-2015)." > pronto/README.txt

# Download the ZIP file into the data directory.
curl -fL "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip" \
  -o pronto/data/open_data_year_one.zip

# Extract the ZIP archive into the data directory.
unzip -o pronto/data/open_data_year_one.zip -d pronto/data

# Display the first ten lines of the trip data CSV.
trip_file=$(find pronto/data -type f -name '2015_trip_data.csv' -print -quit)
if [[ -z "$trip_file" ]]; then
  echo "Error: 2015_trip_data.csv was not found after unzipping." >&2
  exit 1
fi
head "$trip_file"
