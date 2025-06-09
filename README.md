# 🌏 TravelBuddy

**From start to end, we’re your friend.**

TravelBuddy is your smart, AI-powered travel assistant that helps you plan, organize, and enjoy your trips — stress-free. Whether you’re hopping between cities or exploring hidden gems, TravelBuddy’s got your back!

---

## ✨ Features

- 🧠 Multi-agent AI system for smart itinerary planning
- 🗺️ Personalized travel plans based on user preferences
- 🧳 Destination discovery with local insights
- ⏱️ Time-optimized scheduling with real-time adjustments
- 💬 Natural language chat for planning and suggestions
- 📍 Map integration for seamless navigation

---

## 🚀 Getting Started

### Add .env file under root directory
```.env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
LLM_MODEL=gemini-2.0-flash
GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
SERPAPI_API_KEY=<YOUR_SERPAPI_API_KEY>
```

### Install Requirements

```bash
git clone https://github.com/engkeong-sve/travel_buddy.git
cd travel_buddy

# Install dependencies
pip install -r requirements.txt

# Run agent with adk web
adk web
```
