# 🌏 TravelBuddy

**From start to end, we’re your friend.**

Travel Buddy is your smart, AI-powered travel assistant that helps you plan, organize, and enjoy your trips — stress-free. Whether you’re hopping between cities or exploring hidden gems, Travel Buddy’s got your back!

---

## ✨ Features

- 🧠 Multi-agent AI system for smart itinerary planning
- 🗺️ Personalized travel plans based on user preferences
- 🧳 Destination discovery with local insights
- ⏱️ Time-optimized scheduling with real-time adjustments
- 💬 Natural language chat for planning and suggestions
- 📍 Map integration for seamless navigation

---

## How does it work?

Travel Buddy is a multi-agent AI system built using Google Agent Development Kit (ADK). It has a manager agent that delegates tasks to multiple sub-agents and tools, ensuring a seamless coordination among the sub-agents to curate a personalized itinerary just for you. 

### List of Sub-Agents
- 🏨 Hotel Agent
- ✈️ Flight Agent
- 🗺️ Attraction Spot Agent
- 🍽️ Restaurant Agent
- 🧭 Routing Agent
- 📄 Template Agent
- ☀️ Weather Agent
- 🎒 Packing Agent

### List of Tools
- 📧 Send Email
- ⏰ Add User Reminder Item
- 📥 Receive User Reminder Item
- 📝 Get User Reminder List

---

## 🚀 Getting Started

### Add .env file under root directory
```.env
# Language Model Configuration
GOOGLE_GENAI_USE_VERTEXAI=FALSE
LLM_MODEL=gemini-2.5-flash
LLM_TEMPERATURE=0.1

# API Keys
GOOGLE_API_KEY=<your_google_api_key>
SERPAPI_API_KEY=<your_serpapi_api_key>

# Email (SMTP) Configuration
EMAIL_ADDRESS=<your_gmail_address>
EMAIL_APP_PASSWORD=<your_gmail_app_password>
```

### Install Requirements

```bash
git clone https://github.com/engkeong-sve/travel_buddy.git
cd travel_buddy

# Install dependencies
pip install -r requirements.txt
```

### Run Travel Buddy

You may use Git Bash to run the script below to automatically start the application.

```bash
bash run_travel_buddy.sh
```

Alternatively, use the command below.
```bash
cd backend/itinerary-agent/
adk api_server
cd ../../frontend/
streamlit run app.py
```
