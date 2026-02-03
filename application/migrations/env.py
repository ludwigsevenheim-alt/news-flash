"""Alembic environment configuration."""
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.database import db

config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

target_metadata = db.metadata

def run_migrations_offline():
    url = os.environ.get('DATABASE_URL', 'sqlite:///news_flash.db')
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    url = os.environ.get('DATABASE_URL', 'sqlite:///news_flash.db')
    configuration = {"sqlalchemy.url": url}
    connectable = engine_from_config(configuration, prefix="sqlalchemy.", poolclass=pool.StaticPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

