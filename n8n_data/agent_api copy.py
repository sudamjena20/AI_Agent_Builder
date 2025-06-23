from fastapi import FastAPI
import requests
from google_calendar import check_and_book_slot
import json
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import re

load_dotenv()

app = FastAPI()


class Message(BaseModel):
    message: str

GEMINI_API_URL = "Your_API_URL"  # Replace with your actual Gemini API URL
GEMINI_API_KEY = os.getenv("Your_API_KEY")

@app.post("/agent")
async def agent_handler(message: Message):
    user_msg = message.message

    # Send to Gemini
    gemini_prompt = f"""You are AI agent if someone trying to send any message try to do more conversation so that you can gather all necessary information.

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
        # Extract JSON block from markdown string
        text_block = gemini_json["candidates"][0]['content']['parts'][0]['text']
        # Remove markdown code block markers and any leading 'json'
        json_str = re.sub(r"^```json|^```|```$", "", text_block, flags=re.MULTILINE).strip()
        # Now parse the JSON string
        gemini_text = json.loads(json_str)
    except Exception as e:
        print("Error processing Gemini response:", e)
        return {"reply": "Sorryyy brother, there was an error processing your request."}

    print('gemini type', gemini_text)

    subject = gemini_text.get("subject")
    date = gemini_text.get("date")
    time = gemini_text.get("time")
    # print(gemini_dict["candidate"][0]['content']["parts"][0]["text"])
    if not (subject and date and time):
        return {"reply": "Sorryyy brother, I could not extract meeting details."}

    # Check and book slot
    booking_reply = check_and_book_slot(subject, date, time)
    return {"reply": booking_reply}