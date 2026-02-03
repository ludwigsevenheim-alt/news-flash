"""
Public routes - accessible without authentication.

This blueprint handles all public-facing pages including the landing page.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.database import db
from app.data.models.subscriber import Subscriber

bp = Blueprint("public", __name__)


@bp.route("/")
def index():
    """Render the landing page."""
    return render_template("index.html")


@bp.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    """Handle subscription form."""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        
        if name and email:
            subscriber = Subscriber(name=name, email=email)
            db.session.add(subscriber)
            db.session.commit()
            return redirect(url_for("public.thank_you"))
    
    return render_template("subscribe.html")


@bp.route("/thank-you")
def thank_you():
    """Render thank you page."""
    return render_template("thank_you.html")

