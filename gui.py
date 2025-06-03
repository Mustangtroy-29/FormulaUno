import streamlit as st
import fastf1
from fastf1 import plotting

# Setup FastF1
fastf1.Cache.enable_cache('cache')  # You can change or remove 'cache' dir

# Set page config
st.set_page_config(page_title="Formula Uno", layout="wide")

# Title and description
st.title("🏎️ Formula 1 Data Analysis")
st.markdown("Analyze F1 races, drivers, constructors, and more!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Upload Data", "Race Analysis", "Driver Insights", "Constructor Stats"])

# Upload section
if page == "Upload Data":
    # Select Season (2017–2025)
    season = st.selectbox("Select Season", list(range(2025, 2016, -1)))

    # Fetch and select Grand Prix (Races) for the selected season
    schedule = fastf1.get_event_schedule(season)
    available_gp = schedule["EventName"].tolist()
    selected_gp = st.selectbox("Select Grand Prix", available_gp)

    # Get selected event object
    event = schedule[schedule["EventName"] == selected_gp].iloc[0]
    round_number = event["RoundNumber"]

    # Fetch session types (from FastF1 convention)
    session_options = ["Practice 1", "Practice 2", "Practice 3", "Qualifying", "Sprint", "Race"]
    selected_session = st.selectbox("Select Session", session_options)

    session = fastf1.get_session(season, round_number, selected_session)
    session.load()

    # Try to load session to fetch drivers
    try:
        drivers = session.drivers
        driver_names = [session.get_driver(drv)["Abbreviation"] for drv in drivers]
        selected_driver = st.selectbox("Select Driver", driver_names)
    except Exception as e:
        st.error(f"Could not load session data: {e}")
        selected_driver = None

    # Output selected options
    st.markdown("---")
    st.subheader("🎯 Selected Options")
    st.write(f"**Season:** {season}")
    st.write(f"**Grand Prix:** {selected_gp}")
    st.write(f"**Session:** {selected_session}")
    if selected_driver:
        st.write(f"**Driver:** {selected_driver}")

# Overview section
elif page == "Overview":
    st.header("📊 Overview Dashboard")
    st.markdown("Get a quick summary of your dataset, top races, drivers, etc.")
    # Placeholder charts and stats
    st.info("Upload data first to view insights.")

# Race Analysis
elif page == "Race Analysis":
    st.header("🏁 Race Analysis")
    st.markdown("Explore insights from individual races.")
    st.warning("No data loaded yet.")

# Driver Insights
elif page == "Driver Insights":
    st.header("👨‍✈️ Driver Insights")
    st.markdown("Analyze performance of drivers over seasons.")
    st.warning("No data loaded yet.")

# Constructor Stats
elif page == "Constructor Stats":
    st.header("🏭 Constructor Statistics")
    st.markdown("Compare constructor performance and wins.")
    st.warning("No data loaded yet.")
