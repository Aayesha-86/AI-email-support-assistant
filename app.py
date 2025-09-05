import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("📬 AI-Powered Communication Assistant")
st.subheader("Filtered Support Emails")

# Buttons
if st.button("Seed Demo Emails"):
    response = requests.post(f"{BACKEND_URL}/seed_demo")
    st.write(response.json())

if st.button("Refresh Emails"):
    response = requests.get(f"{BACKEND_URL}/emails")
    emails = response.json()
    if emails:
        for e in emails:
            st.markdown(f"**From:** {e['sender']}")
            st.markdown(f"**Subject:** {e['subject']}")
            st.markdown(f"**Body:** {e['body']}")
            st.markdown("---")
    else:
        st.write("No emails yet. Click 'Seed Demo Emails'.")

# Analytics
if st.button("Show Analytics"):
    response = requests.get(f"{BACKEND_URL}/stats")
    st.write(response.json())
