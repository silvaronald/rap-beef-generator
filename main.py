import streamlit as st
from api import generate_diss_rap

st.set_page_config(page_title="The Beef", page_icon="🥩", layout="centered")
st.title("🎤 Diss Track Generator")

st.markdown("Write how you want your **diss track** to be made, and let **LLMs** do the roasting.")

user_input = st.text_input("🔥 Your diss theme:", placeholder="e.g. Ruthless from the perspective of a WWII soldier")

if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please describe the diss style first!")
    else:
        with st.spinner("Summoning lyrical destruction..."):
            rap = generate_diss_rap(user_input)
            st.success("✅ Rap generated!")
            st.code(rap, language="text")
