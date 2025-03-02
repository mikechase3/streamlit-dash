import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import helpers
from typing import Dict, List, Tuple, Union, Any  # Import necessary types

# Type Aliases for Clarity
LanguageDataFrame = pd.DataFrame
TimelineDataFrame = pd.DataFrame
MatplotlibFigure = plt.Figure

def main() -> None:
    """Main function to run the Streamlit app."""

    st.title("Mike Chase's Computer Science Journey")

    # Load and display language data
    lang_df: LanguageDataFrame = pd.read_csv("data/language-focus-distribution.csv", dtype={"Language": str, "Hours": int})
    languages_pie_chart: MatplotlibFigure = helpers.create_pie_chart(lang_df)
    st.pyplot(languages_pie_chart)
    st.dataframe(lang_df)

    # Load and display timeline data
    timeline_df: TimelineDataFrame = pd.read_csv("data/timeline_data.csv", dtype={"Year": str, "Month": str, "Title": str, "Description": str})

    st.subheader("Timeline of Events")

    for _, row in timeline_df.iterrows():
        helpers.create_timeline_entry(row["Year"], row["Month"], row["Title"], row["Description"])

    st.markdown("---")  # Separator


if __name__ == "__main__":
    main()  # Call the main function

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