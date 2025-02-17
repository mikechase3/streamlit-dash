import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart(df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.pie(df["Hours"], labels=df["Language"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    plt.title("Language Focus Distribution (Hours)")
    return fig

def display_data(df: pd.DataFrame, subheader: str):
    st.subheader(subheader)
    st.dataframe(df)

