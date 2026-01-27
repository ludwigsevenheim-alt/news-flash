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

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev-secret-key")
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
