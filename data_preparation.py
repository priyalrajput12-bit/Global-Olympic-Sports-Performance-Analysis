import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/athlete_events.csv")

print("Original Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing numerical values
for col in ["Age", "Height", "Weight"]:
    df[col] = df[col].fillna(df[col].median())

# Handle missing medal values
df["Medal"] = df["Medal"].fillna("No Medal")

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/olympic_cleaned.csv", index=False)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:", df.shape)
print("\nData preparation completed successfully!")
