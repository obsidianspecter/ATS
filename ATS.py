import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

def main():
    # App title
    st.title("📊 ATS Project Management Dashboard")

    # Comprehensive Dashboard View
    display_dashboard()

# Comprehensive Dashboard View
def display_dashboard():
    st.header("🌟 ATS Project Plan and Timeline")

    # Project Overview Section
    st.subheader("📌 Project Overview")
    st.markdown(
        """
        **About ATS**
        An Applicant Tracking System (ATS) is a recruitment solution designed to simplify and enhance hiring processes. It automates repetitive tasks and provides insightful, data-driven decision-making tools.

        ### Key Objectives:
        - 🛠️ **Streamline job posting creation** with user-friendly tools.
        - 🤖 **Automate resume parsing** and AI-driven scoring.
        - 🎯 **Generate tailored interview questions** through AI.
        - 📊 **Analyze skill and educational gaps** efficiently.
        - ✉️ **Keep candidates engaged** with automated communication updates.

        With the ATS, recruitment workflows are redefined to save time and improve hiring quality.
        """
    )

    # Deliverables
    st.subheader("🚀 Final Deliverables")
    st.markdown(
        """
        - **📝 Job Posting Tool**: Create and publish job posts effortlessly.
        - **📂 Candidate Database**: Manage all applicant details in one place.
        - **🤖 AI Resume Scoring**: Evaluate and rank candidates automatically.
        - **📊 Skill Gap Analysis Module**: Pinpoint candidate gaps against job requirements.
        - **💬 Interview Generator**: Create tailored interview questions via AI.
        - **✉️ Automated Communication**: Provide real-time updates to candidates.
        """
    )

    # Team Allocation Section
    st.subheader("👥 Team Allocation and Work Distribution")

    # Team Data
    team_data = pd.DataFrame({
        "Phase": ["Planning", "Resume Parsing", "Skill Gap Analysis", "Interview Generation", "Candidate Ranking", "Automated Communication"],
        "UI/UX Team": ["Abdul Azees P N, Arjun Krishna R, Jaspreet", "-", "-", "-", "-", "-"],
        "Web Team": ["Ahalya, Diviksha, Divya, Sivadharshini, Subashini", "Ahalya, Diviksha, Sivadharshini", "Subashini, Divya", "Diviksha, Sivadharshini", "Ahalya, Divya", "Subashini, Sivadharshini"],
        "AI Team": ["-", "Ayana K, Chris Nevin K Dence", "Ayana K, Chris Nevin K Dence", "Ayana K, Chris Nevin K Dence", "Ayana K, Chris Nevin K Dence", "-"]
    })

    team_data_melted = team_data.melt(id_vars="Phase", var_name="Team", value_name="Members")
    team_data_melted = team_data_melted[team_data_melted["Members"] != "-"]  # Remove rows with no members

    fig_team_chart = px.bar(
        team_data_melted,
        x="Phase",
        y="Members",
        color="Team",
        title="🔄 Detailed Work Assignments by Team",
        labels={"Members": "Team Members"},
        barmode="group",
        height=500
    )

    st.plotly_chart(fig_team_chart, use_container_width=True)

    # Timeline Section
    st.subheader("📅 Project Timeline")

    timeline_data = pd.DataFrame({
        "Phase": ["Planning", "Resume Parsing", "Skill Gap Analysis", "Interview Generation", "Candidate Ranking", "Communication"],
        "Start Date": [
            datetime(2025, 1, 15),
            datetime(2025, 1, 25),
            datetime(2025, 2, 5),
            datetime(2025, 2, 15),
            datetime(2025, 2, 25),
            datetime(2025, 3, 5)
        ],
        "End Date": [
            datetime(2025, 1, 24),
            datetime(2025, 2, 4),
            datetime(2025, 2, 14),
            datetime(2025, 2, 24),
            datetime(2025, 3, 4),
            datetime(2025, 3, 15)
        ]
    })

    fig_timeline = px.timeline(
        timeline_data,
        x_start="Start Date",
        x_end="End Date",
        y="Phase",
        title="⏳ Project Timeline",
        color="Phase",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_timeline.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig_timeline)

    st.markdown(
        """### Timeline Highlights:
        - **Planning**: Jan 15 - Jan 24
        - **Resume Parsing**: Jan 25 - Feb 4
        - **Skill Gap Analysis**: Feb 5 - Feb 14
        - **Interview Generation**: Feb 15 - Feb 24
        - **Candidate Ranking**: Feb 25 - Mar 4
        - **Communication**: Mar 5 - Mar 15
        """
    )

    # Phase Progress Section
    st.subheader("📈 Phase Progress")

    phases = ["Planning", "Resume Parsing", "Skill Gap Analysis", "Interview Generation", "Candidate Ranking", "Communication"]
    progress = [80, 60, 40, 20, 10, 0]  # Sample progress percentages

    fig_progress = go.Figure(go.Bar(
        x=phases,
        y=progress,
        marker_color='lightskyblue',
        text=progress,
        textposition='outside',
    ))
    fig_progress.update_layout(
        title="📊 Project Phase Progress",
        xaxis_title="Phases",
        yaxis_title="Progress (%)",
        yaxis=dict(range=[0, 100]),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_progress)

if __name__ == "__main__":
    main()
