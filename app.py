import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import helpers

# Load the skills data
skills_df = pd.read_csv("skills.csv")

# Streamlit app title
st.title("My Computer Science Journey")

# Sample skills data (replace with your actual data)
languages_data = {
    'Language': ['Python', 'Java', 'C', 'Golang', 'JavaScript', 'CSS', 'HTML'],
    'Hours': [1000, 1000, 10, 10, 10, 10, 100]
}
languages_df = pd.DataFrame(languages_data)
st.pyplot(helpers.create_pie_chart(languages_df))

# Display the raw data
st.subheader("Language Focus Distribution (Hours)")
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