import streamlit as st
import pandas as pd
import altair as alt
import base64

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

# Add a "Submit" button
if st.button("Submit"):
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

    # Display a line chart of the mood rating over time
    chart_data = mood_data[["date", "rating"]]
    chart = alt.Chart(chart_data).mark_line().encode(
        x="date:T",
        y="rating:Q"
    ).properties(
        width=600,
        height=400,
        title="Mood Rating Over Time"
    )
    st.altair_chart(chart)

# Display the user's mood rating and notes for the selected date
st.write("You rated your mood on", selected_date, "as", mood_rating)
if notes:
    st.write("Notes:", notes)
else:
    st.write("No notes added.")

# Add a download button for the mood data
def download_csv():
    csv_file = mood_data.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mood_data.csv">Download Mood Data</a>'
    return href

st.markdown(download_csv(), unsafe_allow_html=True)

