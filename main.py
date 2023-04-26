import streamlit as st
import plotly.express as px
from backend import get_data
import streamlit as st
from datetime import datetime as dt


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

    with today:
        st.title(now.strftime("%B %d, %I:%M %p"))
        date_today = now.strftime("%Y-%m-%d")
        todays_data = data[date_today]
        sky_conditions = []

        # css tags to remove delta arrow from st.metric()
        st.write(
            """
            <style>
            [data-testid="stMetricDelta"] svg {
                display: none;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        for point in todays_data:
            temp = point["main"]["temp"]
            feel = point["main"]["feels_like"]
            sky_condition = point["weather"][0]["main"]

            col1, mid, col2 = st.columns([1, 1, 1])

            with col1:
                st.metric("Temperature", f"{(temp/10):.2f} °C", delta=f"Feels like {(feel/10):.2f} °C",
                          delta_color="off", help=None, label_visibility="visible", )

            with col2:
                st.image(images[sky_condition],
                         width=175, caption=sky_condition)

    with tomorrow:
        st.title("Tomorrow's Weather Forecast")

    with fivedays:
        st.title("Weather Forecast for the Next Five Days")

# st.title("Weather Forecast for the Next Days")
# location = st.text_input("City/Country: ")
# days = st.slider("Forecast Days", min_value=1, max_value=5,
#                  help="Select the number of forecasted days")
# option = st.selectbox("Select data to view", ("Temperature", "Sky",))
# st.subheader(f"{option} for the next {days} days in {location}")

# if location:
#     # get temperature/sky data
#     while True:
#         try:
#             data = get_data(location, days)
#             break
#         except:
#             st.warning('The City/Country does not exist!', icon="⚠️")
#             # st.write("City/Country does not exist")
#             st.stop()

#     if option == "Temperature":
#         temperatures = [reading["main"]["temp"] /
#                         10 for reading in data]
#         dates = [reading["dt_txt"] for reading in data]
#         # Create temperature plot
#         figure = px.line(x=dates, y=temperatures, labels={
#             "x": "Date", "y": "Temperature"})
#         # gets figure object as input. Alternate libraries: Plotly, Bokeh
#         st.plotly_chart(figure)
#     elif option == "Sky":
#         sky_conditionss = [reading["weather"][0]["main"]
#                           for reading in data]
#         images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
#                   "Rain": "images/rain.png", "Snow": "images/snow.png"}
#         imagepaths = [images[condition] for condition in sky_conditionss]
#         st.image(imagepaths, width=100)
