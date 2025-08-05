import streamlit as st
import random

# Custom CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=UnifrakturCook:wght@700&display=swap');

        body {
            background-color: #ffe6f0;
        }
        .main {
            background-color: #ffe6f0 !important;
        }
        h1.gothic-title {
            font-family: 'UnifrakturCook', cursive;
            text-align: center;
            font-size: 4em;
            margin-bottom: 0.2em;
            color: #000000;
        }
        .roast-text {
            font-family: 'Special Elite', monospace;
            font-size: 1.6em;
            color: #cc0066;
            text-align: center;
            padding: 1em;
        }
        .stButton>button {
            background-color: #ff66b2;
            color: white;
            padding: 0.75em 2em;
            font-size: 1.3em;
            border-radius: 12px;
            display: block;
            margin: 0 auto;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #ff3385;
        }
        img {
            display: block;
            margin: 0 auto 20px auto;
        }
    </style>
""", unsafe_allow_html=True)

# Display glitter heart image
st.image("https://raw.githubusercontent.com/your-username/roast-jake/main/IMG_3731.png", width=200)

# Title and subtitle
st.markdown("<h1 class='gothic-title'>Feeling sad?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Click below for a dopamine hit — at Jake’s expense.</p>", unsafe_allow_html=True)

# Load roasts
@st.cache_data
def load_roasts():
    with open("roasts.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

roasts = load_roasts()

# Button
if st.button("Roast Jake"):
    st.markdown(f"<div class='roast-text'>{random.choice(roasts)}</div>", unsafe_allow_html=True)
