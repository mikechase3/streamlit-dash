import streamlit as st
import pandas as pd
import helpers
from typing import Dict, List, Tuple, Union, Any  # Import necessary types


# Streamlit app title
st.title("Mike Chase's Computer Science Journey")

# Load the lang data
lang_df = pd.read_csv("data/language-focus-distribution.csv", dtype={"Language": str, "Hours": int})

languages_pie_chart = helpers.create_pie_chart(lang_df)
st.pyplot(languages_pie_chart)
st.dataframe(lang_df)

# Load the timeline data
timeline_df = pd.read_csv("data/timeline_data.csv", dtype={"Year": str, "Month": str, "Title": str, "Description": str})
st.subheader("Timeline of Events")

def create_timeline_entry(year, month, title, description): # Include month
    col1, col2, col3 = st.columns([1, 2, 5])  # Adjust column ratios as needed

    with col1:
        st.write(f"**{year}**")  # Year in bold

    with col2:
        if month: # Check if month exists
            st.write(f"**{month}**")
        else:
            st.write("")

    with col3:
        st.write(f"**{title}**")  # Title in bold
        st.write(description)  # Description


for _, row in timeline_df.iterrows():
    create_timeline_entry(row["Year"], row["Month"], row["Title"], row["Description"])

# Add a horizontal line to separate entries (optional)
st.markdown("---")

# DEBUGGING ONLY
# def main():
#     st.title("My App")
#
#     lang_df = pd.read_csv("data/language-focus-distribution.csv", dtype={"Language": str, "Hours": int})
#
#     st.write("Here's the DataFrame:")
#     st.write(lang_df)
#
#     languages_pie_chart = helpers.create_pie_chart(lang_df)
#     st.pyplot(languages_pie_chart)
#     st.dataframe(lang_df)
#
# if __name__ == "__main__":
#     st.set_page_config(initial_sidebar_state="expanded")
#     st.session_state.ran = True
#     main()