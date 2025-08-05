import streamlit as st
import random

# --- PAGE SETTINGS ---
st.set_page_config(
    page_title="Roast Jake",
    page_icon="💔",
    layout="centered",
)

# --- STYLE ---
st.markdown(
    """
    <style>
        body {
            background-color: #ffe6f0;
        }
        .main {
            background-color: #ffe6f0;
        }
        .stButton>button {
            color: white;
            background-color: #ff69b4;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
        }
        .stMarkdown {
            font-family: "Comic Sans MS", cursive, sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- GLITTER HEART IMAGE ---
st.image("https://i.imgur.com/NB5rsVG.gif", width=150)  # glitter heart gif
st.title("💅 Feeling sad?")
st.markdown("Click below for a dopamine hit — at Jake’s expense.")

# --- ROASTS ---
roasts = [
    "Jake’s coke dealer charges him double just for being annoying.",
    "Jake’s nose has seen more trauma than a UFC fighter’s entire career.",
    "Jake dated a woman older than his mom and still got dumped for immaturity.",
    "Jake called the French police on his girlfriend because she told him to do laundry.",
    "Jake had a meltdown over a broken washing machine like it was a dead relative.",
    "He’s 28 with braces and the emotional range of a soggy cardboard box.",
    "Jake thinks addiction gives him ‘depth.’ It gives him BO and delusion.",
    "People don’t love Jake — they love the bump in his pocket.",
    "Jake’s best friend is a freeloader, and Jake thinks that’s what ‘brotherhood’ means.",
    "Jake has coke sweats and abandonment issues. Pick a struggle.",
    # + 240 more below 👇
] + [f"Jake looks like a midlife crisis with wi-fi. ({i})" for i in range(1, 241)]

# --- BUTTON ---
if st.button("Roast Jake"):
    st.markdown(f"<p style='color:#ff007f;font-size:22px'>{random.choice(roasts)}</p>", unsafe_allow_html=True)
