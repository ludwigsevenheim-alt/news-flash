"""Subscriber model for database persistence."""
from app.database import db
from datetime import datetime


class Subscriber(db.Model):
    """Subscriber model representing a user subscription."""
    
    __tablename__ = "subscribers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    subscribed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Subscriber {self.email}>"
