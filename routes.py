from fastapi import APIRouter
from .db import SessionLocal
from .models import Email
from datetime import datetime

router = APIRouter()

# Seed demo emails
@router.post("/seed_demo")
def seed_demo():
    db = SessionLocal()
    demo_emails = [
        {"sender": "alice@example.com", "subject": "Order delay", "body": "My order is delayed."},
        {"sender": "bob@example.com", "subject": "Refund request", "body": "I want a refund."},
        {"sender": "charlie@example.com", "subject": "Product inquiry", "body": "Is this item in stock?"},
    ]
    for e in demo_emails:
        db.add(Email(
            sender=e["sender"],
            subject=e["subject"],
            body=e["body"],
            received_at=datetime.utcnow()
        ))
    db.commit()
    db.close()
    return {"status": "Demo emails seeded successfully!"}

# Get all emails
@router.get("/emails")
def get_emails():
    db = SessionLocal()
    emails = db.query(Email).all()
    db.close()
    return [{"id": e.id, "sender": e.sender, "subject": e.subject, "body": e.body} for e in emails]

# Get analytics/stats
@router.get("/stats")
def stats():
    db = SessionLocal()
    total = db.query(Email).count()
    db.close()
    return {"total_emails": total}
