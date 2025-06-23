import streamlit as st
import requests

# Custom CSS for better design
st.markdown("""
    <style>
    body {
        background: #f7f7fa;
    }
    .main {
        background: #f7f7fa;
    }
    .chat-container {
        max-width: 500px;
        margin: 40px auto 0 auto;
        background: #fff;
        border-radius: 18px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        padding: 32px 24px 24px 24px;
    }
    .chat-bubble-user {
        background: #e0f7fa;
        color: #222;
        padding: 12px 18px;
        border-radius: 18px 18px 4px 18px;
        margin-bottom: 10px;
        align-self: flex-end;
        max-width: 80%;
        font-size: 16px;
    }
    .chat-bubble-bot {
        background: #f3e5f5;
        color: #222;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 4px;
        margin-bottom: 10px;
        align-self: flex-start;
        max-width: 80%;
        font-size: 16px;
    }
    .chat-header {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 18px;
        color: #4a148c;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #bdbdbd;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7b1fa2 0%, #f06292 100%);
        color: #fff;
        border-radius: 8px;
        font-size: 16px;
        padding: 8px 24px;
        border: none;
        margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chat-container">
    <div class="chat-header">
        Welcome to the AI Agent Demo
    </div>
    <div style="text-align:center; margin-top:30px; color:#666; font-size:18px;">
        This is a demo website for showcasing the AI Agent.
    </div>
</div>
""", unsafe_allow_html=True)

# Optionally, keep the n8n widget at the bottom
import streamlit.components.v1 as components
components.html(
    """<script type="module">
      import Chatbot from "https://cdn.n8nchatui.com/v1/embed.js";
      Chatbot.init({
        n8nChatUrl: "http://localhost:5678/webhook/44cfc099-0c8f-4c13-b210-a25838401506/chat",
        metadata: {},
        theme: {
          button: {
            backgroundColor: "#ffc8b8",
            right: 20,
            bottom: 20,
            size: 50,
            iconColor: "#373434",
            customIconSrc: "https://www.svgrepo.com/show/339963/chat-bot.svg",
            customIconSize: 60,
            customIconBorderRadius: 15,
            autoWindowOpen: {
              autoOpen: false,
              openDelay: 2
            },
            borderRadius: "rounded"
          },
          tooltip: {
            showTooltip: true,
            tooltipMessage: "Hello! Welcome to Modelos AI Agent. How can I help you?",
            tooltipBackgroundColor: "#fff9f6",
            tooltipTextColor: "#1c1c1c",
            tooltipFontSize: 15
          },
          chatWindow: {
            borderRadiusStyle: "rounded",
            avatarBorderRadius: 24,
            messageBorderRadius: 25,
            showTitle: true,
            title: "Modelos AI Agent Chatbot",
            titleAvatarSrc: "https://www.svgrepo.com/show/339963/chat-bot.svg",
            welcomeMessage: "Hello! Welcome to Modelos AI Agent.",
            errorMessage: "For any other information connect to help@test.com",
            backgroundColor: "#ffffff",
            height: 600,
            width: 400,
            fontSize: 16,
            starterPrompts: [
              "How can I help you?"
            ],
            starterPromptFontSize: 15,
            renderHTML: false,
            clearChatOnReload: false,
            botMessage: {
              backgroundColor: "#514b68",
              textColor: "#fafafa",
              showAvatar: true,
              avatarSrc: "https://www.svgrepo.com/show/334455/bot.svg"
            },
            userMessage: {
              backgroundColor: "#7aff70",
              textColor: "#050505",
              showAvatar: true,
              avatarSrc: "https://www.svgrepo.com/show/532363/user-alt-1.svg"
            },
            textInput: {
              placeholder: "Type your query",
              backgroundColor: "#ffffff",
              textColor: "#1e1e1f",
              sendButtonColor: "#f36539",
              maxChars: 50,
              maxCharsWarningMessage: "You exceeded the characters limit. Please input less than 50 characters.",
              autoFocus: false,
              borderRadius: 6,
              sendButtonBorderRadius: 50
            },
            uploadsConfig: {
              enabled: true,
              acceptFileTypes: [
                "jpeg",
                "jpg",
                "png",
                "pdf"
              ],
              maxFiles: 5,
              maxSizeInMB: 10
            },
            voiceInputConfig: {
              enabled: true,
              maxRecordingTime: 15,
              recordingNotSupportedMessage: "To record audio, use modern browsers like Chrome or Firefox that support audio recording"
            }
          }
        }
      });
    </script>
    """,
    height=700,
)