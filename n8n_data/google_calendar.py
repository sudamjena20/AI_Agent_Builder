from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        "/home/sudam/Downloads/n8n_data/credentials.json",
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    return build("calendar", "v1", credentials=creds)

def check_and_book_slot(subject, date, time):
    service = get_calendar_service()
    # Compose RFC3339 datetime
    event_start = datetime.datetime(2025, 6, 16, 17, 0).isoformat() + "Z"  # 5:00 PM UTC
    event_end = datetime.datetime(2025, 6, 16, 18, 0).isoformat() + "Z"  # 6:00 PM UTC

    # Check for existing events
    events = service.events().list(
        calendarId="primary",
        timeMin=event_start,
        timeMax=event_end,
        singleEvents=True
    ).execute()

    if events.get("items"):
        return f"The slot at {time} on {date} is not available."

    # Book event

    event = {
        "summary": subject,
        "start": {"dateTime": event_start, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": event_end, "timeZone": "Asia/Kolkata"},
        "conferenceData": {
            "createRequest": {
                "requestId": f"{subject}-{date}-{time}".replace(" ", "-"),
                "conferenceSolutionKey": {"type": "hangoutsMeet"}
            }
        },
    "attendees": [
        {"email": "jenasudam950@gmail.com"}  # Replace with your actual email
    ]
    }
    created_event = service.events().insert(
        calendarId="primary",
        body=event,
        conferenceDataVersion=1,
        sendUpdates="all"
    ).execute()
    meet_link = created_event.get("conferenceData", {}).get("entryPoints", [{}])[0].get("uri", "No Meet link generated")
    return f"Your meeting '{subject}' is booked for {date} at {time}! Google Meet link: {meet_link}"
