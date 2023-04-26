import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky",))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    # get temperature/sky data
    filtered_data = get_data(place, days)
    if option == "Temperature":
        temperatures = [reading["main"]["temp"] for reading in filtered_data]
        dates = [reading["dt_txt"] for reading in filtered_data]
        # Create temperature plot
        figure = px.line(x=dates, y=temperatures, labels={
            "x": "Date", "y": "Temperature"})
        # gets figure object as input. Alternate libraries: Plotly, Bokeh
        st.plotly_chart(figure)
    elif option == "Sky":
        filtered_data = [reading["weather"][0]["main"]
                         for reading in filtered_data]
        st.image()
