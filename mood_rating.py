import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the mood data from a CSV file
mood_data = pd.read_csv("mood_data.csv")

# Display a header and subheader
st.header("Mood Tracker")
st.subheader("Track your mood over time")

# Use a date picker to select the date to rate
selected_date = st.date_input("Select a date:", pd.to_datetime("today").date())

# Use radio buttons to rate the mood
st.write("Rate your mood:")
mood_rating = st.radio("", [1, 2, 3, 4, 5])

# Add a text input for notes
notes = st.text_input("Add notes (optional):")

# Add the mood rating and notes to the mood data
new_data = {"date": selected_date, "rating": mood_rating, "notes": notes}
mood_data = mood_data.append(new_data, ignore_index=True)

# Save the updated mood data to the CSV file
mood_data.to_csv("mood_data.csv", index=False)

# Display the user's mood rating and notes for the selected date
st.write("You rated your mood on", selected_date, "as", mood_rating)
if notes:
    st.write("Notes:", notes)
else:
    st.write("No notes added.")

# Add a line chart of the mood ratings over time
st.subheader("Mood Ratings Over Time")
sns.lineplot(data=mood_data, x="date", y="rating")
st.pyplot()

# Add a bar chart of the average mood ratings by week
st.subheader("Average Mood Ratings by Week")
mood_data['week'] = mood_data['date'].dt.strftime('%Y-%U')
weekly_ratings = mood_data.groupby('week')['rating'].mean().reset_index()
bar_chart = px.bar(weekly_ratings, x='week', y='rating')
st.plotly_chart(bar_chart)
