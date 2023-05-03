# weather-webapp-streamlit

This project started out as my attempt at recreating my phone's weather app. I am done with most of the backend work, all that's left is styling the UI. Currently on hold since I'll need to learn CSS to create the UI I want.
</br>

Weather data is fetched from the [OpenWeather API](https://openweathermap.org/api), I am using their [5 Day / 3 Hour Forecast](https://openweathermap.org/forecast5) package. You will need their API key to run this project in real time. If you don't want to use any API, I have sample data in `filter_by_day.json`. Just replace the API calls in `backend.py` with `json.load(open("filter_by_day.json",))`.

 
### Current UI:
 <img src="https://github.com/sadpotat/weather-webapp-streamlit/blob/main/for_readme/screenshot.JPG?raw=true" width="75%">
 </br>

### Tagget UI:
 <img src="https://github.com/sadpotat/weather-webapp-streamlit/blob/main/for_readme/ui_target.png?raw=true" width="75%">
 
 This UI is a design by [Denny D](https://dribbble.com/shots/14096604-Weather-dashboard).
 </br>

### Requirements:
- An API key for OpenWeather. [Sign up here](https://home.openweathermap.org/users/sign_up).
- Streamlit module
- Datetime module
