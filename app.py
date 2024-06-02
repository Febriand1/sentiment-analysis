import streamlit as st
from auth.login import login
from auth.register import register
from auth.auth import logout, switch_to
from page.data_500 import show_500_data
from page.data_1000 import show_1000_data

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'view' not in st.session_state:
    st.session_state['view'] = "login"

if st.session_state['authentication_status']:
    st.sidebar.title(f"Welcome {st.session_state['username']}")

    select = st.sidebar.selectbox(
        "Choose a Data",
        ["500 Data", "1000 Data"]
    )

    if select == "500 Data":
        show_500_data()
    elif select == "1000 Data":
        show_1000_data()

    st.sidebar.button("Logout", key="logout_button", on_click=logout)

else:
    if st.session_state['view'] == "login":
        login()
        if st.sidebar.button("Register", key="register_button", on_click=lambda: switch_to("register")):
            pass
    elif st.session_state['view'] == "register":
        register()
        if st.sidebar.button("Login", key="back_to_login_button", on_click=lambda: switch_to("login")):
            pass