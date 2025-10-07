import streamlit as st
import pandas as pd
import plotly.express as px
# penguin dataset
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')


st.set_page_config(
    page_title="Interactive Penguin Dashboard",
    page_icon="🐧",
    layout="wide",
)

st.title("🐧 Interactive Penguin Dashboard")
st.write("Explore data from the Palmer Penguins dataset.")


st.sidebar.header("Dashboard Filters")


species = st.sidebar.multiselect(
    "Select the Species:",
    options=df["species"].unique(),
    default=df["species"].unique()
)


sex = st.sidebar.multiselect(
    "Select the Sex:",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)


bill_length_range = st.sidebar.slider(
    "Select Bill Length (mm):",
    min_value=float(df['bill_length_mm'].min()),
    max_value=float(df['bill_length_mm'].max()),
    value=(float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max()))
)


df_selection = df.query(
    "species == @species and sex == @sex and bill_length_mm >= @bill_length_range[0] and bill_length_mm <= @bill_length_range[1]"
)


st.subheader("Filtered Data")
st.dataframe(df_selection)

st.write(f"Displaying {df_selection.shape[0]} rows.")


st.subheader("Data Visualizations")


fig = px.scatter(
    df_selection,
    x="bill_length_mm",
    y="bill_depth_mm",
    color="species",
    hover_name="species",
    title="Bill Length vs. Bill Depth"
)
st.plotly_chart(fig, use_container_width=True)