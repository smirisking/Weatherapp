import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days you want to forecast")

option1 = st.selectbox("Select the kind of Temperature scale you want us to use", ("Celsius", "Fahrenheit"))

option = st.selectbox("Select data to view", ("Temperature", "Sky Condition"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)
        if option1 == "Celsius":
            temperatures = [(d["main"]["temp"] / 10) for d in filtered_data]
            y_label = "Temperature (°C)"
        elif option1 == "Fahrenheit":
            temperatures = [((d["main"]["temp"] / 10) * 9 / 5 + 32) for d in filtered_data]
            y_label = "Temperature (°F)"

        if option == "Temperature":
            dates = [d["dt_txt"] for d in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": y_label})
            st.plotly_chart(figure)

        elif option == "Sky Condition":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=115)

    except:
        st.error("You entered a city that doesn't exist. Please check the spelling.")