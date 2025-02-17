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
        Establish a connection to Dropbox using OAuth.
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

    def upload_file(self, local_path, dropbox_path):
        """
        Upload a file to Dropbox.
        """
        try:
            if not os.path.exists(local_path):
                LOGGER.error(f"File not found: {local_path}")
                return False

            with open(local_path, "rb") as f:
                self.dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
            LOGGER.info(f"File {local_path} uploaded to {dropbox_path}")
            return True
        except ApiError as ex:
            LOGGER.error(f"Failed to upload {local_path} to Dropbox: {ex}")
            return False

    def download_file(self, dropbox_path, local_path):
        """
        Download a file from Dropbox.
        """
        try:
            self.dbx.files_download_to_file(local_path, dropbox_path)
            LOGGER.info(f"File {dropbox_path} downloaded to {local_path}")
            return True
        except ApiError as ex:
            LOGGER.error(f"Failed to download {dropbox_path} from Dropbox: {ex}")
            return False


if __name__ == "__main__":
    """
    Main script for testing Dropbox connection, user registration, and file operations.
    """
    dropbox_integration = DropboxIntegration()

    # Example: Register a new user and create their directory structure
    user_name = "test_user"
    user_uuid = "1234-5678-uuid"

    if dropbox_integration.register(user_name, user_uuid):
        LOGGER.info(f"User {user_name} successfully registered in Dropbox.")
    else:
        LOGGER.error(f"Failed to register user {user_name}.")

    # Example: Upload a test file
    local_upload_path = "test.txt"
    dropbox_upload_path = f"/users/{user_uuid}/test.txt"

    upload_success = dropbox_integration.upload_file(local_upload_path, dropbox_upload_path)

    if upload_success:
        LOGGER.info(f"Successfully uploaded {local_upload_path} to Dropbox.")

    # Example: Download the test file
    dropbox_download_path = f"/users/{user_uuid}/test.txt"
    local_download_path = "downloaded_test.txt"

    download_success = dropbox_integration.download_file(dropbox_download_path, local_download_path)

    if download_success:
        LOGGER.info(f"Successfully downloaded {dropbox_download_path} to {local_download_path}.")
