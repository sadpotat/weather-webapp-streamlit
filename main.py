from datetime import datetime as dt, timedelta
import streamlit as st
from backend import get_data, get_12_hour


st.set_page_config(page_title="Weather",
                   page_icon=":sun_with_face:", layout="wide")

location = st.text_input("City/Country: ", placeholder="Enter a location",
                         help="Enter a city or country's name to view its weather forecast")

if location:
    while True:
        try:
            data = get_data(location)
            break
        except:
            st.warning('The City/Country does not exist!', icon="⚠️")
            # st.write("City/Country does not exist")
            st.stop()

    today, tomorrow, fivedays = st.tabs(["Today", "Tomorrow", "Next 5 days"])
    images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
              "Rain": "images/rain.png", "Snow": "images/snow.png"}
    now = dt.now()

    # css tags to remove delta arrow from st.metric()
    st.write(
        """
        <style>
        [data-testid="stMetricDelta"] svg {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True)

    with today:
        st.title(now.strftime("%B %d, %I:%M %p"))
        st.text("")
        st.text("")
        st.text("")
        date_today = now.strftime("%Y-%m-%d")
        todays_data = data[date_today]
        sky_conditions = []

        for point in todays_data:
            temp = point["main"]["temp"]
            feel = point["main"]["feels_like"]
            sky_condition = point["weather"][0]["main"]
            time_now = get_12_hour(point["dt_txt"][11:-3])

            start, col1, col2, end = st.columns([1, 1, 1, 1])

            with col1:
                st.metric(f"{time_now}", f"{(temp/10):.2f} °C", delta=f"Feels like {(feel/10):.2f} °C",
                          delta_color="off", help=None, label_visibility="visible", )

            with col2:
                st.image(images[sky_condition],
                         width=150, caption=sky_condition)

    with tomorrow:
        now = now + timedelta(1)
        st.title(now.strftime("%B %d, %A"))
        st.text("")
        st.text("")
        st.text("")
        date_today = now.strftime("%Y-%m-%d")
        todays_data = data[date_today]
        sky_conditions = []

        for point in todays_data:
            temp = point["main"]["temp"]
            feel = point["main"]["feels_like"]
            sky_condition = point["weather"][0]["main"]
            time_now = get_12_hour(point["dt_txt"][11:-3])

            start, col1, col2, end = st.columns([1, 1, 1, 1])

            with col1:
                st.metric(f"{time_now}", f"{(temp/10):.2f} °C", delta=f"Feels like {(feel/10):.2f} °C",
                          delta_color="off", help=None, label_visibility="visible", )

            with col2:
                st.image(images[sky_condition],
                         width=150, caption=sky_condition)

    with fivedays:
        st.title("Weather Forecast for the Next Five Days")
