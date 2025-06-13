import streamlit as st

st.title("Weather Forcast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days you want to forcast")
option = st.selectbox("Select date to view", ("Temperature", "Sky Condition"))

st.subheader(f"{option} for the next {days} days in {place}")