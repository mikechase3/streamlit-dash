import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Union, Any  # Import necessary types

# Type Aliases for Clarity
LanguageDataFrame = pd.DataFrame
TimelineDataFrame = pd.DataFrame
MatplotlibFigure = plt.Figure

# --- Helper Functions ---

def create_pie_chart(df: LanguageDataFrame) -> MatplotlibFigure:
    """Creates and returns a pie chart of language distribution."""
    fig, ax = plt.subplots()
    ax.pie(df["Hours"], labels=df["Language"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    plt.title("Language Focus Distribution (Hours)")
    return fig


def create_timeline_entry(year: str, month: Union[str, None], title: str, description: str) -> None:
    """Creates and displays a single timeline entry using Streamlit columns."""
    col1, col2, col3 = st.columns([1, 2, 5])  # Adjust column ratios as needed

    with col1:
        st.write(f"**{year}**")

    with col2:
        if month:
            st.write(f"**{month}**")
        else:
            st.write("")  # Explicitly write an empty string for consistent spacing

    with col3:
        st.write(f"**{title}**")
        st.write(description)