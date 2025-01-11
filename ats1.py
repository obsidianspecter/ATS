import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import json

# File paths for data persistence
TEAM_DATA_FILE = "team_data.json"
TIMELINE_DATA_FILE = "timeline_data.json"
PROGRESS_DATA_FILE = "progress_data.json"

# Load data from JSON files
def load_data(file_path, default_data):
    try:
        with open(file_path, "r") as f:
            return pd.DataFrame(json.load(f))
    except FileNotFoundError:
        return pd.DataFrame(default_data)

# Save data to JSON files
def save_data(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data.to_dict(orient="records"), f)

# Default Data
team_data_default = {
    "Phase": ["Planning", "Resume Parsing", "Skill Gap Analysis", "Interview Generation", "Candidate Ranking", "Automated Communication"],
    "UI/UX Team": ["Abdul Azees P N, Arjun Krishna R, Jaspreet", "-", "-", "-", "-", "-"],
    "Web Team": ["Ahalya, Diviksha, Divya, Sivadharshini, Subashini", "Ahalya, Diviksha, Sivadharshini", "Subashini, Divya", "Diviksha, Sivadharshini", "Ahalya, Divya", "Subashini, Sivadharshini"],
    "AI Team": ["-", "Ayana K, Chris Nevin K Dence", "Ayana K, Chris Nevin K Dence", "Ayana K, Chris Nevin K Dence", "Ayana K, Chris Nevin K Dence", "-"]
}

timeline_data_default = {
    "Phase": ["Planning", "Resume Parsing", "Skill Gap Analysis", "Interview Generation", "Candidate Ranking", "Communication"],
    "Start Date": [
        datetime(2025, 1, 15).strftime("%Y-%m-%d"),
        datetime(2025, 1, 25).strftime("%Y-%m-%d"),
        datetime(2025, 2, 5).strftime("%Y-%m-%d"),
        datetime(2025, 2, 15).strftime("%Y-%m-%d"),
        datetime(2025, 2, 25).strftime("%Y-%m-%d"),
        datetime(2025, 3, 5).strftime("%Y-%m-%d")
    ],
    "End Date": [
        datetime(2025, 1, 24).strftime("%Y-%m-%d"),
        datetime(2025, 2, 4).strftime("%Y-%m-%d"),
        datetime(2025, 2, 14).strftime("%Y-%m-%d"),
        datetime(2025, 2, 24).strftime("%Y-%m-%d"),
        datetime(2025, 3, 4).strftime("%Y-%m-%d"),
        datetime(2025, 3, 15).strftime("%Y-%m-%d")
    ]
}

progress_data_default = {
    "Phase": ["Planning", "Resume Parsing", "Skill Gap Analysis", "Interview Generation", "Candidate Ranking", "Communication"],
    "Progress (%)": [80, 60, 40, 20, 10, 0]
}

# Load data
team_data = load_data(TEAM_DATA_FILE, team_data_default)
timeline_data = load_data(TIMELINE_DATA_FILE, timeline_data_default)
progress_data = load_data(PROGRESS_DATA_FILE, progress_data_default)

# Streamlit Dashboard
st.title("📊 ATS Project Management Dashboard")

# Team Allocation Section
st.subheader("👥 Team Allocation and Work Distribution")
phase_filter = st.selectbox("Filter by Phase", ["All"] + team_data["Phase"].unique().tolist())

if phase_filter == "All":
    st.dataframe(team_data)
else:
    st.dataframe(team_data[team_data["Phase"] == phase_filter])

# Timeline Section with Plotly
st.subheader("📅 Project Timeline")
timeline_chart = px.timeline(timeline_data, x_start="Start Date", x_end="End Date", y="Phase", color="Phase",
                             title="Project Timeline", color_discrete_sequence=px.colors.qualitative.Set3)
timeline_chart.update_yaxes(categoryorder="total ascending")
st.plotly_chart(timeline_chart)

# Progress Section with Plotly
st.subheader("📈 Phase Progress")
progress_chart = px.bar(progress_data, x="Phase", y="Progress (%)", color="Phase",
                        title="Phase Progress", text="Progress (%)", color_discrete_sequence=px.colors.sequential.Viridis)
progress_chart.update_layout(yaxis=dict(range=[0, 100]))
st.plotly_chart(progress_chart)

# Add/Edit and Export functionality
def export_data(df, filename):
    df.to_csv(filename, index=False)
    st.success(f"{filename} exported successfully!")

if st.button("Export Team Data"):
    export_data(team_data, "team_data.csv")

if st.button("Export Timeline Data"):
    export_data(timeline_data, "timeline_data.csv")

if st.button("Export Progress Data"):
    export_data(progress_data, "progress_data.csv")
