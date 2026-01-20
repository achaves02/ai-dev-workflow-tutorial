import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="ShopSmart Sales Dashboard",
    page_icon="📊",
    layout="wide"
)


# Data loading function with caching
@st.cache_data
def load_data():
    """Load sales data from CSV file."""
    try:
        df = pd.read_csv("data/sales-data.csv", parse_dates=["date"])
        return df
    except FileNotFoundError:
        return None


# Load data
df = load_data()

# Error handling for missing CSV file
if df is None:
    st.error("Data file not found. Please ensure data/sales-data.csv exists.")
    st.stop()

# Error handling for empty data
if df.empty:
    st.warning("No data available to display.")
    st.stop()

# Dashboard title
st.title("ShopSmart Sales Dashboard")

# --- User Story 1: Key Performance Indicators ---

# Calculate KPI metrics
total_sales = df["total_amount"].sum()
total_orders = df["order_id"].nunique()

# Create two-column layout for KPI metrics
col1, col2 = st.columns(2)

# Display Total Sales with currency formatting
with col1:
    st.metric(label="Total Sales", value=f"${total_sales:,.0f}")

# Display Total Orders with number formatting
with col2:
    st.metric(label="Total Orders", value=f"{total_orders:,}")
