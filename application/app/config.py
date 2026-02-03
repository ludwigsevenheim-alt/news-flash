"""
Application configuration using dataclasses.

Configuration is loaded from environment variables with sensible defaults
for development. In production, set SECRET_KEY to a secure random value.
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Base configuration."""

    # Dessa två rader är de som efterfrågas i Step 1
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("DATABASE_URL", "sqlite:///news_flash.db")
    
    DEBUG: bool = False
    TESTING: bool = False


@dataclass
class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG: bool = True


@dataclass
class TestingConfig(Config):
    """Testing configuration."""

    TESTING: bool = True


@dataclass
class ProductionConfig(Config):
    """Production configuration."""

    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}