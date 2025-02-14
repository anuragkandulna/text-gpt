from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from utils.custom_logger import CustomLogger
from utils.psql_database import DatabaseConnection
from sqlalchemy.ext.declarative import declarative_base

# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=20).get_logger()

# Get SQLAlchemy base
Base = declarative_base()

# Get SQLAlchemy session
db_conn = DatabaseConnection()
SessionLocal = db_conn.get_sqlalchemy_session()


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


def create_new_user(username, password_hash):
    """
    Create a new user in the database.
    """
    session = SessionLocal()
    try:
        user = User(
            username=username,
            email=username,  # Assuming email is the same as username for now
            password_hash=password_hash,
            role=None,
            is_active=True,
        )

        session.add(user)
        session.commit()
        LOGGER.info(f"User {username} created successfully.")
        return user

    except Exception as ex:
        session.rollback()
        LOGGER.error(f"Failed to create new user: {ex}")
        raise

    finally:
        session.close()


def get_user_id(username):
    """
    Fetch the user ID for a given username.
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        return user.user_id if user else None

    except Exception as ex:
        LOGGER.error(f"Failed to fetch user ID: {ex}")
        raise

    finally:
        session.close()


def find_by_username(username):
    """
    Retrieve user details by username.
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            return {
                "username": user.username,
                "email": user.email,
                "password_hash": user.password_hash,
                "is_active": user.is_active,
            }
        return None

    except Exception as ex:
        LOGGER.error(f"Failed to fetch user data: {ex}")
        raise

    finally:
        session.close()