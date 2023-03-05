import privateData
import pickle
from googleapiclient.discovery import apiclient, gflags, httplib2, oauth2client, uritemplate
from datetime import datetime, timedelta

# # setup google calendar
# from google_auth_oauthlib.flow import InstalledAppFlow
# # OAuth API register
# scopes = ['https://www.googleapis.com/auth/calendar']
# flow = InstalledAppFlow.from_client_secrets_file("desktop.json", scopes=scopes)
# credentials = flow.run_console()
# pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

def add_event_to_calendar(CALENDAR_ID, event_summary, event_start_time, event_end_time):
    # Event details
    event = {
      'summary': event_summary,
      'description': "updated : "+ str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')),
      'start': {
        'dateTime': event_start_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'timeZone': 'Asia/Bangkok',
      },
      'end': {
        'dateTime': event_end_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'timeZone': 'Asia/Bangkok',
      },
    }

    # Call the Calendar API to add the event
    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

def clearEvent(CALENDAR_ID):
  page_token = None
  while True:
    events = service.events().list(calendarId=CALENDAR_ID, pageToken=page_token).execute()
    for event in events['items']:
      service.events().delete(calendarId=CALENDAR_ID, eventId=event["id"]).execute()
    page_token = events.get('nextPageToken')
    if not page_token:
      break
