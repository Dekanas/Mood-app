import streamlit as st
import pandas as pd

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

# Create a new DataFrame for the current mood rating
new_data = pd.DataFrame({
    "date": [selected_date],
    "rating": [mood_rating],
    "notes": [notes]
})

# Concatenate the existing mood data with the new data
mood_data = pd.concat([mood_data, new_data], ignore_index=True)

# Save the updated mood data to the CSV file
mood_data.to_csv("mood_data.csv", index=False)

# Display the user's mood rating and notes for the selected date
st.write("You rated your mood on", selected_date, "as", mood_rating)
if notes:
    st.write("Notes:", notes)
else:
    st.write("No notes added.")
