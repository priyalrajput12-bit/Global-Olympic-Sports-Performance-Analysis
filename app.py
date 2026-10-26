import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Olympic Performance Dashboard",
    layout="wide"
)

st.title("Global Olympic Sports Performance Analysis")
st.write("Explore Olympic athletes, sports and medal records.")

@st.cache_data
def load_data():
    return pd.read_csv("data/olympic_cleaned.csv")

df = load_data()

# Filters
years = sorted(df["Year"].dropna().unique())

selected_years = st.sidebar.slider(
    "Select Olympic Year Range",
    int(min(years)),
    int(max(years)),
    (int(min(years)), int(max(years)))
)

filtered_df = df[
    (df["Year"] >= selected_years[0]) &
    (df["Year"] <= selected_years[1])
]

# Key metrics
c1, c2, c3 = st.columns(3)

c1.metric("Total Athlete Records", f"{len(filtered_df):,}")
c2.metric("Sports", filtered_df["Sport"].nunique())
c3.metric("Olympic Years", filtered_df["Year"].nunique())

# Medal distribution
st.subheader("Medal Distribution")

medal_df = filtered_df[
    filtered_df["Medal"].isin(["Gold", "Silver", "Bronze"])
]

medal_counts = medal_df["Medal"].value_counts().reset_index()
medal_counts.columns = ["Medal", "Count"]

fig1 = px.bar(
    medal_counts,
    x="Medal",
    y="Count",
    title="Olympic Medal Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# Top countries by medal records
st.subheader("Top 10 Countries by Medal Records")

top_countries = (
    medal_df.groupby("NOC")
    .size()
    .reset_index(name="Medal Records")
    .sort_values("Medal Records", ascending=False)
    .head(10)
)

fig2 = px.bar(
    top_countries,
    x="NOC",
    y="Medal Records",
    title="Top 10 NOCs by Medal Records"
)

st.plotly_chart(fig2, use_container_width=True)

# Athlete participation
st.subheader("Athlete Participation Over the Years")

participation = (
    filtered_df.groupby("Year")["ID"]
    .nunique()
    .reset_index(name="Athletes")
)

fig3 = px.line(
    participation,
    x="Year",
    y="Athletes",
    markers=True,
    title="Athlete Participation by Year"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Olympic dashboard loaded successfully!")
