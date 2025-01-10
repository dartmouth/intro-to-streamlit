import streamlit as st
import pandas as pd
import seaborn as sns


@st.cache_data
def get_data():
    return sns.load_dataset("penguins")


df = get_data()

selected_species = st.multiselect(
    label="Species",
    options=df.species.unique(),
    default=df.species.unique(),
)

subset = df[df.species.isin(selected_species)]

with st.expander(label="Data"):
    subset

st.scatter_chart(
    subset,
    x="bill_depth_mm",
    y="bill_length_mm",
    color="species",
)
