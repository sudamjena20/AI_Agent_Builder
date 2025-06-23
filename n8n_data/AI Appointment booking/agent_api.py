from fastapi import FastAPI
import requests
from google_calendar import check_and_book_slot
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import re

load_dotenv()

app = FastAPI()

class Message(BaseModel):
    message: str

GEMINI_API_URL = "Your_API_URL"
GEMINI_API_KEY = os.getenv("Your_API_KEY")

@app.post("/agent")
async def agent_handler(message: Message):
    user_msg = message.message

    # Send to Gemini
    gemini_prompt = f"""You are an AI agent. If someone sends a message, try to continue the conversation to gather all necessary information for booking a meeting.

Message: {user_msg}
"""
    try:
        gemini_resp = requests.post(
            GEMINI_API_URL,
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": gemini_prompt}
                        ]
                    }
                ]
            }
        )
        gemini_resp.raise_for_status()
        gemini_json = gemini_resp.json()
        text_block = gemini_json["candidates"][0]['content']['parts'][0]['text']
    except Exception as e:
        print("Error processing Gemini response:", e)
        return {"reply": "Sorry, there was an error processing your request."}

    # Extract meeting details
    subject = None
    date = None
    time = None
    duration = None
    email = None

    subject_match = re.search(r"Subject:\s*(.*)", text_block)
    date_match = re.search(r"Date:\s*(.*)", text_block)
    time_match = re.search(r"Time:\s*(.*)", text_block)
    duration_match = re.search(r"Duration:\s*(.*)", text_block)
    email_match = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", text_block)

    if subject_match: subject = subject_match.group(1).strip()
    if date_match: date = date_match.group(1).strip()
    if time_match: time = time_match.group(1).strip()
    if duration_match: duration = duration_match.group(1).strip()
    if email_match: email = email_match.group(1).strip()

    if subject and date and time and duration and email:
        # Pass all details to booking function
        booking_reply = check_and_book_slot(subject, date, time, duration, email)
        return {"reply": booking_reply}
    else:
        # Continue the conversation with Gemini's response
        return {"reply": text_block}
