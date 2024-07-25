import os

# Generate a secure secret key
SECRET_KEY = os.urandom(24).hex()

# Example SQLALCHEMY_DATABASE_URI configuration for SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'superset.db')

# Optional: Additional configurations can go here

