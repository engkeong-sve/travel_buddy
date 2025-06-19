import streamlit as st
import requests
import os
import uuid 

BACKEND_URL = os.getenv('BACKEND_URL',"http://127.0.0.1:8000")

st.set_page_config(page_title="Travel Buddy", layout="centered")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Travel Buddy 🧳✈️")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Hey! How can I assist you to craft a perfect travel itinerary?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(user_input)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    session_id = st.session_state.session_id

    first_payload = {
        "name": "test",
    }

    response = requests.post(
            f"{BACKEND_URL}/apps/itinerary_agent/users/user_001/sessions/{session_id}",
            json=first_payload,
            headers={"Content-Type": "application/json"}
    )

    # Prepare API request payload
    payload = {
        "appName": "itinerary_agent",
        "userId": "user_001",
        "sessionId": session_id,
        "newMessage": {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    }

    # Send the request to the API
    try:
        response = requests.post(
            f"{BACKEND_URL}/run",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        # response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print(data)

        # bot_response = data[0]['content']['parts'][0]['text']

        for content in data:
            parts = content.get('content', {}).get('parts', [])

            for part in parts:
                if 'text' in part:
                    bot_response = part['text']
                    # Display assistant response in chat message container
                    with st.chat_message("ai"):
                        st.markdown(bot_response.strip())
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "ai", "content": bot_response.strip()})


                elif 'functionCall' in part:
                    function_call = part['functionCall']['name']        
                    with st.chat_message("function", avatar="🛠️"):
                        st.markdown(f"`{function_call}` is called")
                    st.session_state.messages.append({"role": "function", "content":f"`{function_call}` is called"})


    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred. Please try again later. Error: {str(e)}"
        with st.chat_message("ai"):
            st.markdown("There was an error processing your request. Please try again later.")
        st.session_state.messages.append({"role": "ai", "content": "There was an error processing your request. Please try again later."})
