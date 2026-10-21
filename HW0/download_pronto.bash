
#!/bin/bash

# Go to the script directory
cd "$(dirname "$0")" || exit 1

# Create directories
mkdir -p pronto/data

# Create README.txt
echo "Pronto bike-share data for Seattle, including trip, station, weather, and status information." > pronto/README.txt

# Download the data
curl -L https://s3.amazonaws.com/pronto-data/open_data_year_one.zip -o pronto/data/open_data_year_one.zip

# Unzip the file
unzip -o pronto/data/open_data_year_one.zip -d pronto/data

# Show the first few lines
head pronto/data/2015_trip_data.csv

