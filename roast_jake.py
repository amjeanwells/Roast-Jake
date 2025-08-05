import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Roast Jake",
    page_icon="💔",
    layout="centered",
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bubblegum+Sans&display=swap');

        html, body, [class*="css"] {
            font-family: 'Bubblegum Sans', cursive;
            background-color: #ffe6f0;
        }

        .centered-button .stButton>button {
            display: block;
            margin: 0 auto;
            background-color: #ff69b4;
            color: white;
            border-radius: 20px;
            padding: 12px 24px;
            font-size: 20px;
            font-weight: bold;
        }

        .roast-text {
            color: #ff007f;
            font-size: 24px;
            text-align: center;
            padding-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- LOAD ROASTS FROM FILE ---
@st.cache_data
def load_roasts():
    with open("roasts.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

roasts = load_roasts()

# --- DISPLAY HEADER IMAGE ---
st.image("https://raw.githubusercontent.com/amjeanwells/roast-jake/main/IMG_3137.png", width=200)

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>💅 Feeling sad?</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Click below for a dopamine hit — at Jake’s expense.</h4>", unsafe_allow_html=True)

# --- ROAST BUTTON ---
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Roast Jake"):
            st.markdown(f"<div class='roast-text'>{random.choice(roasts)}</div>", unsafe_allow_html=True)
