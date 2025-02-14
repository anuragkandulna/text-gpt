from datetime import datetime
import uuid
import re
import validators
from sqlalchemy import Column, String, Integer, Boolean, DateTime
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


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    audio_segment_len = Column(Integer, nullable=False, default=0)
    src_video_lang = Column(String, nullable=False)
    src_video_title = Column(String, nullable=True)
    src_video_len_hr = Column(Integer, nullable=False, default=0)
    src_video_len_min = Column(Integer, nullable=False, default=0)
    src_video_len_sec = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    translate_to_lang = Column(String, nullable=True)
    num_segments = Column(Integer, nullable=False, default=0)
    audio_dir = Column(String, nullable=True)
    transcription_dir = Column(String, nullable=True)
    translation_dir = Column(String, nullable=True)
    summary_dir = Column(String, nullable=True)
    final_transcript_file = Column(String, nullable=True)
    final_translation_file = Column(String, nullable=True)
    final_summary_file = Column(String, nullable=True)

    @staticmethod
    def is_valid_youtube_url(url):
        """
        Verify if the given URL is a valid YouTube URL.
        """
        youtube_regex = (
            r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/"
            r"(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
        )
        return validators.url(url) and bool(re.match(youtube_regex, url))


def create_project(title, url, audio_segment_len, src_video_lang):
    """
    Create a new project and add it to the database.
    """
    if not Project.is_valid_youtube_url(url):
        raise ValueError("Invalid YouTube URL")

    session = SessionLocal()
    try:
        project = Project(
            title=title,
            url=url,
            audio_segment_len=audio_segment_len,
            src_video_lang=src_video_lang,
            audio_dir=f"./{uuid.uuid4()}/audio/",
            transcription_dir=f"./{uuid.uuid4()}/transcriptions/",
            translation_dir=f"./{uuid.uuid4()}/translations/",
            summary_dir=f"./{uuid.uuid4()}/summaries/",
        )

        session.add(project)
        session.commit()
        LOGGER.info(f"Project {title} created successfully.")
        return project

    except Exception as ex:
        session.rollback()
        LOGGER.error(f"Error while creating project {title}: {ex}")
        raise

    finally:
        session.close()


def fetch_project(project_id):
    """
    Fetch a project by its ID.
    """
    session = SessionLocal()
    try:
        return session.query(Project).filter(Project.project_id == project_id).first()

    except Exception as ex:
        LOGGER.error(f"Error fetching project {project_id}: {ex}")
        raise

    finally:
        session.close()


def update_project(project_id, updates):
    """
    Update a project with new details.
    """
    session = SessionLocal()
    try:
        project = session.query(Project).filter(Project.project_id == project_id).first()
        if not project:
            return None

        for key, value in updates.items():
            setattr(project, key, value)

        project.updated_at = datetime.utcnow()
        session.commit()
        LOGGER.info(f"Updated project {project_id} with {updates}.")
        return project

    except Exception as ex:
        session.rollback()
        LOGGER.error(f"Error updating project {project_id}: {ex}")
        raise

    finally:
        session.close()


def delete_project(project_id):
    """
    Soft delete a project by setting is_deleted to True.
    """
    session = SessionLocal()
    try:
        project = session.query(Project).filter(Project.project_id == project_id).first()
        if project:
            project.is_deleted = True
            project.updated_at = datetime.utcnow()
            session.commit()
            LOGGER.info(f"Project {project_id} marked as deleted.")
            return True
        return False

    except Exception as ex:
        session.rollback()
        LOGGER.error(f"Error marking project {project_id} as deleted: {ex}")
        raise

    finally:
        session.close()