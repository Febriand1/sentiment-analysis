import streamlit as st

def logout():
    st.session_state['authentication_status'] = None
    st.session_state['username'] = ""
    switch_to("login")

def switch_to(value):
    st.session_state['view'] = value