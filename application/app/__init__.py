"""
News Flash - Application Factory

This module creates and configures the Flask application using the
application factory pattern. This pattern enables:
- Multiple instances with different configurations
- Easy testing with test configurations
- Delayed configuration loading
"""

import os

from flask import Flask

from .config import config


def create_app(config_name: str | None = None) -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config_name: Configuration to use ('development', 'testing', 'production').
                    Defaults to FLASK_ENV environment variable or 'development'.

    Returns:
        Configured Flask application instance.
    """
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "development")

    app = Flask(
        __name__,
        template_folder="presentation/templates",
        static_folder="presentation/static",
    )

    # Load configuration
    app.config.from_object(config[config_name])
    
# Register blueprints
    from .presentation.routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    return app
