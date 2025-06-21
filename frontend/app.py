import streamlit as st
import requests
import os
import uuid 
import base64
from PIL import Image
from dotenv import load_dotenv
import random
from waiting_msg import WAITING_MSG 

load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title="Travel Buddy",
    page_icon="✈️",
    layout="centered"
)

# --- Constants ---
BACKEND_URL = os.getenv('BACKEND_URL')

# --- CSS Loader ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

image_path = "assets/travel_buddy_logo.png"

if os.path.exists(image_path):
    st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: center; gap: 2rem; margin-top: 2rem;">
            <img src="data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" width="80">
            <h1 style="color: #FFD700; margin: 0;">Travel Buddy 🧳✈️</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error("Logo not found!")


st.markdown("</div>", unsafe_allow_html=True)

if "user_id" not in st.session_state:
    st.session_state.user_id = "user_" + str(uuid.uuid4())

# --- Session State Initialization ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    
    user_id = st.session_state.user_id
    session_id = st.session_state.session_id
    
    try:
        requests.post(
            f"{BACKEND_URL}/apps/itinerary_agent/users/{user_id}/sessions/{session_id}",
            json={},
            headers={"Content-Type": "application/json"}
        )
    except requests.exceptions.RequestException as e:
        print(f"Error initializing session: {e}")
        st.error("Failed to initialize session. Please try again later.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if user_input := st.chat_input("Hey! How can I assist you to craft a perfect travel itinerary?"):
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    user_id = st.session_state.user_id
    session_id = st.session_state.session_id

    # Display loading spinner with a random dad joke
    random_joke = random.choice(WAITING_MSG)
    with st.spinner(f"{random_joke}"):
        # --- Send Chat Message to Backend ---
        payload = {
            "appName": "itinerary_agent",
            "userId": user_id,
            "sessionId": session_id,
            "newMessage": {
                "role": "user",
                "parts": [{"text": user_input}]
            }
        }

        try:
            print("posting to backend", payload)
            response = requests.post(
                f"{BACKEND_URL}/run",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            data = response.json()

            print("response from backend", data)
            for content in data:
                parts = content.get('content', {}).get('parts', [])
                for part in parts:
                    if 'text' in part:
                        bot_response = part['text'].strip()
                        with st.chat_message("ai"):
                            st.markdown(bot_response)
                        st.session_state.messages.append({"role": "ai", "content": bot_response})

                    elif 'functionCall' in part:
                        function_call = part['functionCall']['name']
                        with st.chat_message("function", avatar="🛠️"):
                            st.markdown(f"`{function_call}` is called")
                        st.session_state.messages.append({"role": "function", "content": f"`{function_call}` is called"})

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            error_msg = "There was an error processing your request. Please try again later."
            with st.chat_message("ai"):
                st.markdown(error_msg)
            st.session_state.messages.append({"role": "ai", "content": error_msg})

# --- Footer ---
st.markdown("""
    <div class="footer">
        ✈️ Travel Buddy &copy; 2025 — From start to end, we are your friend!
    </div>
""", unsafe_allow_html=True)
