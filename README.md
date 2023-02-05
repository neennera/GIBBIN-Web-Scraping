# GIBBIN-Web-Scraping
Web scraping by Python.

# Tools
- HTML
- CSS
- JavaScript
- google clound API

# Function

# Google clound API setup
For who want to create their own calendar. you can follow these step.
0. Ask me to add you to the test user group.
1. Create your API keys
    - create app "GIBBIN" in https://console.cloud.google.com/
    - enable "Google Calendar API" & "Analytics Hub API"
    - create app and goto "OAuth consent screen"
    - set Publishing status:Testing , User type:External, Test users: this email
    - add scope '.../auth/userinfo.email', '.../auth/userinfo.profile', 'openid', '	.../auth/analytics.edit', '.../auth/calendar'
    - create "OAuth 2.0 Client IDs" Credentials(Desktop type). names "Desktop client 1"
    - dowload OAuth.json and open in google colab
    - get token follow : "https://www.youtube.com/watch?v=j1mh0or2CX8&t=153s"
    - save token and use "service = build("calendar", "v3", credentials=credentials)" to create google calendar service
2. Create calendar in Google calendar
    - create calendar and get CALENDAR_ID
3. Change API_KEY & CALENDAR_ID
