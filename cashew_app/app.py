import streamlit as st
from home import home_page
from classifier import classifier_page

# Maintain page state
if "step" not in st.session_state:
    st.session_state.step = 0    # 0 = home, 1 = classifier

if st.session_state.step == 0:
    home_page()
else:
    classifier_page()
