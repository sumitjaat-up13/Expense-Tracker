import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

API_URL = "https://web-production-523d5.up.railway.app"

st.title("Expense Tracking System")

tab1,tab2 = st.tabs(["Add/Update","Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()



