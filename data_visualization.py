import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Olympic dataset
df = pd.read_csv("data/athlete_events.csv")

# Create folder for charts
os.makedirs("visualizations", exist_ok=True)

# 1. Medal Distribution
medals = df["Medal"].dropna().value_counts()

medals.plot(kind="bar")
plt.title("Olympic Medal Distribution")
plt.xlabel("Medal Type")
plt.ylabel("Number of Medals")
plt.tight_layout()
plt.savefig("visualizations/medal_distribution.png")
plt.close()

# 2. Top 10 Countries by Medal Records
top_countries = (
    df.dropna(subset=["Medal"])
    .groupby("NOC")["Medal"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

top_countries.plot(kind="bar")
plt.title("Top 10 Countries by Olympic Medal Records")
plt.xlabel("Country Code")
plt.ylabel("Medal Records")
plt.tight_layout()
plt.savefig("visualizations/top_countries.png")
plt.close()

# 3. Athlete Participation by Year
participation = df.groupby("Year")["ID"].nunique()

participation.plot(kind="line", marker="o")
plt.title("Athlete Participation Over the Years")
plt.xlabel("Olympic Year")
plt.ylabel("Number of Athletes")
plt.tight_layout()
plt.savefig("visualizations/athlete_participation.png")
plt.close()

print("All three visualizations have been created successfully!")
