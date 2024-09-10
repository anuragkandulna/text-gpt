"""
Project data model.
"""

from datetime import datetime
import uuid
from utils.psql_database import DatabaseConnection
from utils.custom_logger import CustomLogger


# Invoke LOGGER
LOGGER = CustomLogger(__name__, level=10).get_logger()
DB_CONN = DatabaseConnection()


class Project:
    def __init__(self):
        self.project_id = ""
        self.title = ""
        self.url = ""
        self.audio_segment_len = 0
        self.src_video_lang = ""
        self.src_video_title = ""
        self.src_video_len = (0, 0, 0)  # (hr, min, sec)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
        self.translate_to_lang = ""
        self.num_segments = 0
        self.audio_dir = ""
        self.transcription_dir = ""
        self.translation_dir = ""
        self.summary_dir = ""
        self.seg_audio_files = []
        self.seg_transcript_files = []
        self.seg_translation_files = []
        self.seg_summary_files = []
        self.final_transcript_file = ""
        self.final_translation_file = ""
        self.final_summary_file = ""


    @staticmethod
    def _get_table_name():
        """Return the table name for projects."""
        return 'projects'


    @classmethod
    def create_project(cls, title, url, audio_segment_len, src_video_lang):
        """
        Create a new project in the PostgreSQL database.
        """
        project_id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = created_at

        # Initialize directories using project_id as root
        audio_dir = f"./{project_id}/audio/"
        transcription_dir = f"./{project_id}/transcriptions/"
        translation_dir = f"./{project_id}/translations/"
        summary_dir = f"./{project_id}/summaries/"

        # Prepare project data for insertion
        project_data = {
            "project_id": project_id,
            "title": title,
            "url": url,
            "audio_segment_len": audio_segment_len,
            "src_video_lang": src_video_lang,
            "created_at": created_at,
            "updated_at": updated_at,
            "is_deleted": False,
            "audio_dir": audio_dir,
            "transcription_dir": transcription_dir,
            "translation_dir": translation_dir,
            "summary_dir": summary_dir
        }

        insert_query = f"""
            INSERT INTO {cls._get_table_name()} 
            (project_id, title, url, audio_segment_len, src_video_lang, created_at, updated_at, is_deleted, 
            audio_dir, transcription_dir, translation_dir, summary_dir)
            VALUES (%(project_id)s, %(title)s, %(url)s, %(audio_segment_len)s, %(src_video_lang)s, 
            %(created_at)s, %(updated_at)s, %(is_deleted)s, %(audio_dir)s, %(transcription_dir)s, 
            %(translation_dir)s, %(summary_dir)s)
        """

        try:
            with DB_CONN as db:
                db.execute_query(insert_query, project_data)
                LOGGER.info(f"Project {project_id} created and inserted into the database.")

        except Exception as ex:
            LOGGER.error(f"Error while creating project {title}: {ex}")
            raise


    @classmethod
    def fetch_project(cls, project_id):
        """
        Fetch a project by its ID from the PostgreSQL database.
        """
        query = f"SELECT * FROM {cls._get_table_name()} WHERE project_id = %s"

        try:
            with DB_CONN as db:
                result = db.fetch_data(query, (project_id,))
                if result:
                    LOGGER.info(f"Fetched project data: {result}")
                    return result[0]  # Return the first (and likely only) result
                else:
                    LOGGER.info(f"No project found with ID: {project_id}")
                    return None

        except Exception as ex:
            LOGGER.error(f"Error fetching project {project_id}: {ex}")
            raise


    @classmethod
    def update_project(cls, project_id, updates):
        """
        Update project details in the PostgreSQL database.
        """
        updates['updated_at'] = datetime.now()
        set_clause = ", ".join([f"{key} = %({key})s" for key in updates])
        update_query = f"""
            UPDATE {cls._get_table_name()}
            SET {set_clause}
            WHERE project_id = %(project_id)s
        """

        try:
            with DB_CONN as db:
                result = db.execute_query(update_query, {**updates, "project_id": project_id})
                LOGGER.info(f"Updated project {project_id} with {updates}.")
                return result

        except Exception as ex:
            LOGGER.error(f"Error updating project {project_id}: {ex}")
            raise


    @classmethod
    def delete_project(cls, project_id):
        """
        Soft delete a project by setting is_deleted to True in the PostgreSQL database.
        """
        delete_query = f"""
            UPDATE {cls._get_table_name()}
            SET is_deleted = TRUE, updated_at = %(updated_at)s
            WHERE project_id = %(project_id)s
        """
        try:
            with DB_CONN as db:
                db.execute_query(delete_query, {"project_id": project_id, "updated_at": datetime.now()})
                LOGGER.info(f"Project {project_id} marked as deleted.")

        except Exception as ex:
            LOGGER.error(f"Error marking project {project_id} as deleted: {ex}")
            raise
