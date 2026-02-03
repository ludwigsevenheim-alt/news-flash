"""
Gunicorn entry point for production deployment.

Usage:
    gunicorn wsgi:app

The FLASK_ENV environment variable controls which configuration
class is loaded (development, testing, or production).
"""

from app import create_app

app = create_app()
