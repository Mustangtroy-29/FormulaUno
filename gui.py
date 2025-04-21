import streamlit as st

# Set page config
st.set_page_config(page_title="F1 Analysis App", layout="wide")

# Title and description
st.title("🏎️ Formula 1 Data Analysis")
st.markdown("Analyze F1 races, drivers, constructors, and more!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Upload Data", "Race Analysis", "Driver Insights", "Constructor Stats"])

# Upload section
if page == "Upload Data":
    st.header("📤 Upload F1 Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df.head())

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
