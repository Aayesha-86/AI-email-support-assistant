AI-email-support-assistant (Demo Version)

AI Email Assistant — Documentation
Project Name: AI Email Assistant (Demo Version)
Author: Ayesha Momin
Backend: FastAPI + SQLAlchemy
Frontend: Streamlit
Database: SQLite (via SQLAlchemy)
Purpose: Provide a working demo of the AI Email Assistant without needing real email accounts. Instead of fetching from Gmail, the system loads sample/demo emails into the database and allows drafting and sending simulated replies.

1. Project Overview

The Demo Version of AI Email Assistant allows users to experience the workflow of fetching, drafting, and replying to emails without connecting to real email servers.

Key Features:

Load demo/sample emails into the database

View and interact with emails in the UI

Draft replies to selected emails

Store sent replies in the database (no actual email sending)

Simple, interactive frontend with Streamlit

Same backend architecture (FastAPI + SQLAlchemy), but with mocked email fetching/sending

2. Folder Structure
support-assistant-live/
├─ backend/
│  ├─ __init__.py           # empty, keeps folder as package
│  ├─ main.py               # FastAPI app
│  ├─ routes.py             # API endpoints
│  ├─ db.py                 # Database connection and session
│  ├─ models.py             # SQLAlchemy models
│  ├─ demo_client.py        # Loads demo emails, simulates sending replies
├─ frontend/
│  ├─ app.py                # Streamlit frontend app
├─ requirements.txt         # Python dependencies
└─ README.txt               # Quick instructions

3. Backend Setup
3.1 Dependencies
pip install fastapi uvicorn sqlalchemy streamlit

3.2 Database (db.py)

Uses SQLAlchemy ORM.

Keeps all database logic separate.

Models include Email and DraftResponse.

3.3 Models (models.py)

Email: Stores sender, subject, body, and resolved status.

DraftResponse: Stores email ID and drafted reply.

3.4 Demo Client (demo_client.py)

Instead of IMAP/SMTP:

Loads sample emails into the database (predefined list).

Simulates sending replies → Marks the draft as "sent" in DB.

No real email accounts needed.

3.5 API Routes (routes.py)

Endpoints:

Method	Endpoint	Description
POST	/fetch_emails	Load demo emails into DB
POST	/send_draft/{email_id}	Save reply to DB (simulate sending)

Error handling: JSON responses with status and detail.

3.6 FastAPI App (main.py)

Initializes FastAPI app

Adds CORS middleware

Includes router from routes.py

Creates database tables automatically

4. Frontend Setup
app.py

Built with Streamlit

Talks to backend via HTTP API requests

UI Components:

Fetch Emails Button

Email ID Input

Draft Reply Text Area

Send Draft Button

Example:

import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("📬 AI Email Assistant (Demo)")

if st.button("Fetch Demo Emails"):
    response = requests.post(f"{BACKEND_URL}/fetch_emails")
    st.write(response.json())

email_id = st.number_input("Email ID to reply", min_value=1)
draft_text = st.text_area("Your Draft Reply")

if st.button("Send Draft") and draft_text:
    response = requests.post(
        f"{BACKEND_URL}/send_draft/{email_id}", 
        json={"draft": draft_text}
    )
    st.write(response.json())

5. Environment Variables

⚠️ Not needed in Demo version.

No .env file required.

All emails are sample/demo emails.

6. How to Run the Project
6.1 Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Mac/Linux

6.2 Install Dependencies
pip install -r requirements.txt

6.3 Start Backend
python -m uvicorn backend.main:app --reload

6.4 Start Frontend (new terminal)
streamlit run frontend/app.py

6.5 Usage

Open Streamlit UI → http://localhost:8501

Click Fetch Demo Emails → sample emails stored in DB

Enter Email ID and draft reply

Click Send Draft → reply stored in DB (simulated send)

7. Key Changes vs Real Email Setup

No .env file or credentials needed

demo_client.py replaces email_client.py

Emails are static/demo emails instead of Gmail

Send action is simulated (reply saved in DB only)

8. Notes

Demo version is perfect for testing or showcasing without exposing real inboxes.

Backend must run before frontend.

SQLite DB created automatically on first run.

Demo emails reset each time /fetch_emails is called.
