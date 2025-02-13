import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the skills data
skills_df = pd.read_csv("skills.csv")

# Streamlit app title
st.title("My Computer Science Journey")

# Display the raw data
st.subheader("Skills Data")
st.dataframe(skills_df)

# Group skills by category and calculate average level
average_skills = skills_df.groupby("Category")["Level"].mean().reset_index()

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(average_skills["Category"], average_skills["Level"])
plt.xticks(rotation=45)
plt.ylabel("Average Level")
plt.title("Average Skill Level by Category")

# Display the chart in Streamlit
st.pyplot(fig)

# Add a timeline (you'll need to add your actual timeline data)
st.subheader("Timeline")
st.write("Timeline of my learning journey and projects...")