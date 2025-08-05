import streamlit as st
import random

insults = [
    "Jake once tried to snort Emergen-C.",
    "Jake's reflection avoids him out of embarrassment.",
    "Jake thinks Adderall is a love language.",
    "Jake asked ChatGPT to write his rehab speech.",
    "Jake invested in crypto using a pawned vape pen."
]

st.set_page_config(page_title="Roast Jake", page_icon="💥", layout="centered")

st.markdown("<h1 style='text-align: center;'>Feeling sad?</h1>", unsafe_allow_html=True)
st.write("Click below for a dopamine hit (Jake won’t mind. Probably.)")

if st.button("Roast Jake"):
    st.success(random.choice(insults))
