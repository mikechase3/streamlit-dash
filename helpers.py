import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart(df) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.pie(df["Level"], labels=df["Category"], autopct="%1.1f%%")
    ax.axis("equal")
    return fig

def display_data(df: pd.DataFrame, subheader: str):
    st.subheader(subheader)
    st.dataframe(df)