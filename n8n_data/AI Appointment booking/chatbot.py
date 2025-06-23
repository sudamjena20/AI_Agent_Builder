import streamlit as st
import requests

st.title("Appointment Booking Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")

user_input = st.text_input("Ask me to book a meeting:", key="user_input")

if user_input:
    # Check if the last user message is the same as the current input
    if not (st.session_state.messages and st.session_state.messages[-2][1] == user_input if len(st.session_state.messages) >= 2 else False):
        try:
            response = requests.post(
                "http://localhost:8000/agent",
                json={"message": user_input}
            )
            response.raise_for_status()
            bot_reply = response.json().get("reply", "")

            st.session_state.messages.append(("You", user_input))
            st.session_state.messages.append(("🤖", bot_reply if bot_reply else "No reply."))

            st.rerun()

        except requests.exceptions.RequestException as e:
            st.session_state.messages.append(("🚨", f"Error connecting to FastAPI: {str(e)}"))
            st.rerun()
    else:
        st.warning("You already asked this. Please enter a new message.")
