import pandas as pd
import os

# Dataset file paths
athlete_file = "data/athlete_events.csv"
regions_file = "data/noc_regions.csv"

# Check whether the dataset files exist
if os.path.exists(athlete_file) and os.path.exists(regions_file):

    # Load datasets
    athletes = pd.read_csv(athlete_file)
    regions = pd.read_csv(regions_file)

    print("Olympic datasets loaded successfully!")

    print("\nAthlete Dataset:")
    print(athletes.head())

    print("\nDataset Shape:")
    print("Athlete records:", athletes.shape)
    print("Region records:", regions.shape)

    print("\nColumn Names:")
    print(athletes.columns.tolist())

    print("\nMissing Values:")
    print(athletes.isnull().sum())

else:
    print("Dataset files not found.")
    print("Place both CSV files inside the data folder.")
