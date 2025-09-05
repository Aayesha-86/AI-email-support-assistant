How to Run the Demo:

1. Create a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate  (Windows)
   source .venv/bin/activate  (Mac/Linux)

2. Install requirements:
   pip install -r requirements.txt

3. Start backend:
   python -m uvicorn backend.main:app --reload

4. In a new terminal, start frontend:
   streamlit run frontend/app.py

5. Open the Streamlit URL in your browser, click "Seed Demo Emails".
