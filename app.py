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

# --- User Story 2: Sales Trend Over Time ---

# Create monthly sales aggregation
monthly_sales = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum().reset_index()
monthly_sales["date"] = monthly_sales["date"].dt.to_timestamp()

# Create line chart with markers
fig_trend = px.line(
    monthly_sales,
    x="date",
    y="total_amount",
    markers=True,
    title="Sales Trend Over Time",
    labels={"date": "Month", "total_amount": "Sales ($)"}
)

# Add interactive tooltips showing month and sales amount
fig_trend.update_traces(
    hovertemplate="<b>%{x|%B %Y}</b><br>Sales: $%{y:,.0f}<extra></extra>"
)

# Display chart with full width
st.plotly_chart(fig_trend, use_container_width=True)

# --- User Story 3 & 4: Sales by Category and Region (side-by-side) ---

# Create two-column layout for bar charts
col_category, col_region = st.columns(2)

# Category chart (left column)
with col_category:
    # Create category sales aggregation and sort descending
    category_sales = df.groupby("category")["total_amount"].sum().reset_index()
    category_sales = category_sales.sort_values("total_amount", ascending=False)

    # Create bar chart
    fig_category = px.bar(
        category_sales,
        x="category",
        y="total_amount",
        title="Sales by Category",
        labels={"category": "Category", "total_amount": "Sales ($)"}
    )

    # Add interactive tooltips showing category and sales amount
    fig_category.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>"
    )

    # Display category chart
    st.plotly_chart(fig_category, use_container_width=True)

# Region chart (right column)
with col_region:
    # Create region sales aggregation and sort descending
    region_sales = df.groupby("region")["total_amount"].sum().reset_index()
    region_sales = region_sales.sort_values("total_amount", ascending=False)

    # Create bar chart
    fig_region = px.bar(
        region_sales,
        x="region",
        y="total_amount",
        title="Sales by Region",
        labels={"region": "Region", "total_amount": "Sales ($)"}
    )

    # Add interactive tooltips showing region and sales amount
    fig_region.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>"
    )

    # Display region chart
    st.plotly_chart(fig_region, use_container_width=True)
