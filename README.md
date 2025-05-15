# 🏠 RentWise Matcher

A Smart Property Recommendation System for Renters using LangChain + LLMs + Streamlit

---

## 🚀 Project Overview

**RentWise Matcher** is an intelligent rental matching platform that uses **Large Language Models (LLMs)** and **LangChain** to provide personalized rental property suggestions based on user preferences.

Powered by Streamlit for a seamless UI experience, this app acts as a smart assistant that understands natural language queries like:

> _"I'm looking for a 2BHK flat near Connaught Place under ₹25,000 with a pet-friendly policy."_

And instantly filters the best matches from the available listings.

---

## 📌 Use Case

Traditional real estate platforms provide basic filters and keyword search. But users often think in natural language and want **context-aware recommendations**.

**RentWise Matcher** bridges this gap by:

- Understanding **complex, human-like queries**
- Offering **personalized recommendations**
- Saving **time** and **effort** in the house-hunting process
- Enhancing **user experience** by avoiding repetitive form-based filters

This tool is especially useful for:

- **Renters** looking for homes with specific needs (location, budget, amenities)
- **Real estate platforms** aiming to boost engagement through smart assistants
- **Property managers** to automate matching for leads
- **Startups** building AI-first PropTech solutions

---

## 💡 Key Features

✅ Natural Language Query Input  
✅ LLM + LangChain-powered Filtering  
✅ Streamlit UI with Interactive Inputs  
✅ Smart, Instant Match Recommendations  
✅ Easily Extensible for Other Domains (Jobs, Cars, etc.)

---

## 🧠 Tech Stack

- 🧠 **LangChain** – Framework for building LLM-based applications  
- 💬 **OpenAI / LLM API** – For query understanding and matching logic  
- 🌐 **Streamlit** – Rapid UI prototyping for Python  
- 🐍 **Python** – Core backend logic  
- 📄 **Pandas** – For structured property listings  
- 🏡 (Optional) **Vector DB** – Future integration for embeddings and similarity search

---

## 🏗️ How It Works

1. User enters a natural language query (e.g., location, rent, requirements)
2. LangChain interprets and parses the query into structured filters
3. The app matches and ranks listings using relevance logic
4. Results are displayed instantly with key info and highlights

---

## 📸 Screenshots

> Coming Soon... (Include images of your Streamlit UI output after running)

---

## 🔮 Future Scope

- 🔍 **Semantic Search with Embeddings** for deep matching
- 📍 **Map Integration** for visual location-based results
- 💬 **Chat-based Assistant** using LangChain Agents
- 📱 **Mobile-optimized UI** with deployment on Streamlit Cloud
- 🔁 **Feedback Learning Loop** to improve results based on user likes/dislikes
- 🔗 **Integration with Real Estate APIs** (99acres, MagicBricks, etc.)

## 🧑‍💻 Author
### Satyam Tiwari
### Machine Learning Engineer | Data Science Enthusiast
### 📍 Delhi, India
### 🔗 LinkedIn --https://www.linkedin.com/in/satyam9695/
###✉️ Email: shivt843@gmail.com

---

## 📦 Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/RentWise-Matcher.git
cd RentWise-Matcher

# Create virtual environment and activate
python -m venv venv
venv\Scripts\activate  # On Windows

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run main.py


