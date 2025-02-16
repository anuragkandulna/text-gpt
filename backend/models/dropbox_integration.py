import dropbox
import sys
import os
from dropbox.exceptions import ApiError, AuthError
from utils.dropbox_connect import DropboxConnect
from utils.custom_logger import CustomLogger

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class DropboxIntegration:
    def __init__(self):
        """
        Initialize Dropbox connection and user attributes.
        """
        self.username = ''
        self.user_uuid = ''
        self.project_id = ''
        self.project_title = ''
        self.project_root = ''
        self.audio_dir = ''
        self.transcription_dir = ''
        self.translation_dir = ''
        self.summary_dir = ''
        self.seg_audio_files = []
        self.seg_transcript_files = []
        self.seg_translation_files = []
        self.seg_summary_files = []
        self.final_transcript_file = ''
        self.final_translation_file = ''
        self.final_summary_file = ''
        self.metadata = ''

        # Connect to Dropbox
        self.dbx = None
        self.connect()

    def connect(self):
        """
        Establish a connection to Dropbox.
        """
        try:
            dropbox_client = DropboxConnect()
            self.dbx = dropbox_client.dbx
            account_info = self.dbx.users_get_current_account()
            LOGGER.info(f"Connected to Dropbox as: {account_info.name.display_name}")
        except AuthError:
            LOGGER.critical("ERROR: Invalid Dropbox token. Authentication failed.")
            sys.exit(1)

    def register(self, username, user_uuid):
        """
        Create a new directory structure in Dropbox for a user upon registration.
        """
        try:
            self.username = username
            self.user_uuid = user_uuid
            self.project_root = f"/users/{self.user_uuid}"
            self.audio_dir = f"{self.project_root}/audio/"
            self.transcription_dir = f"{self.project_root}/transcriptions/"
            self.translation_dir = f"{self.project_root}/translations/"
            self.summary_dir = f"{self.project_root}/summaries/"

            # Create folders in Dropbox
            directories = [
                self.project_root,
                self.audio_dir,
                self.transcription_dir,
                self.translation_dir,
                self.summary_dir,
            ]

            for directory in directories:
                try:
                    self.dbx.files_create_folder_v2(directory)
                    LOGGER.info(f"Created folder: {directory}")
                except ApiError as e:
                    if e.error.is_path() and e.error.get_path().is_conflict():
                        LOGGER.warning(f"Folder already exists: {directory}")
                    else:
                        LOGGER.error(f"Failed to create folder {directory}: {e}")

            return True

        except Exception as ex:
            LOGGER.error(f"Error registering user {username}: {ex}")
            return False


if __name__ == '__main__':
    """
    Main script for testing Dropbox connection and registration.
    """
    dropbox_integration = DropboxIntegration()

    # Example user registration
    user_name = "test_user"
    user_uuid = "1234-5678-uuid"

    if dropbox_integration.register(user_name, user_uuid):
        LOGGER.info(f"User {user_name} successfully registered in Dropbox.")
    else:
        LOGGER.error(f"Failed to register user {user_name}.")