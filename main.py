import streamlit as st
import plotly.express as px
from backend import get_data
import streamlit as st

st.set_page_config(page_title="Weather",
                   page_icon=":sun_with_face:", layout="wide")

st.title("Weather Forecast for the Next Days")
location = st.text_input("City/Country: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky",))
st.subheader(f"{option} for the next {days} days in {location}")


if location:
    # get temperature/sky data
    while True:
        try:
            data = get_data(location, days)
            break
        except:
            st.warning('The City/Country does not exist!', icon="⚠️")
            # st.write("City/Country does not exist")
            st.stop()

    if option == "Temperature":
        temperatures = [reading["main"]["temp"] /
                        10 for reading in data]
        dates = [reading["dt_txt"] for reading in data]
        # Create temperature plot
        figure = px.line(x=dates, y=temperatures, labels={
            "x": "Date", "y": "Temperature"})
        # gets figure object as input. Alternate libraries: Plotly, Bokeh
        st.plotly_chart(figure)
    elif option == "Sky":
        sky_conditions = [reading["weather"][0]["main"]
                          for reading in data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        imagepaths = [images[condition] for condition in sky_conditions]
        st.image(imagepaths, width=100)
