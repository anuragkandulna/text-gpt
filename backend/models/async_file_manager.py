import os
import asyncio
import time
from constants.constants import TEMP_TEXTGPT_DIR
from utils.custom_logger import CustomLogger
from models.dropbox_integration import DropboxIntegration
from models.psql_database import DatabaseConnection

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class AsyncFileManager:
    def __init__(self):
        os.makedirs(TEMP_TEXTGPT_DIR, exist_ok=True)
        LOGGER.info(f"TextGPT temp file storage directory created at {TEMP_TEXTGPT_DIR}")

        # Initialize Dropbox connection
        self.dropbox_engine = DropboxIntegration()

        # Initialize DB connection
        self.db_conn = DatabaseConnection()

        # Store already synced files to avoid duplicates
        self.synced_files = set()


    async def scan_and_sync(self):
        """
        Continuously scans TEMP_TEXTGPT_DIR every 5 minutes and syncs new files to Dropbox.
        """
        while True:
            await self.sync_new_files()
            LOGGER.info("Sleeping for 5 minutes before next scan...")
            await asyncio.sleep(300)  # Sleep for 5 minutes


    async def sync_new_files(self):
        """
        Syncs new files and directories to Dropbox.
        """
        try:
            files_to_sync = self.list_files()
            if not files_to_sync:
                LOGGER.info("No new files to sync.")
                return

            LOGGER.info(f"Found {len(files_to_sync)} new files/directories for syncing.")

            for file_path in files_to_sync:
                await self.upload_to_dropbox(file_path)

            await self.cleanup_local_files(files_to_sync)
            await self.update_project_status()

        except Exception as ex:
            LOGGER.error(f"Error during sync operation: {ex}")


    def list_files(self):
        """
        List all files and directories in TEMP_TEXTGPT_DIR.
        """
        new_files = []
        for root, _, files in os.walk(TEMP_TEXTGPT_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path not in self.synced_files:  # Avoid duplicates
                    new_files.append(file_path)
                    self.synced_files.add(file_path)  # Mark as synced
        return new_files


    async def upload_to_dropbox(self, file_path):
        """
        Upload a file to Dropbox.
        """
        try:
            dropbox_path = f"/TextGPT/{os.path.basename(file_path)}"
            upload_success = self.dropbox_engine.upload_file(file_path, dropbox_path)

            if upload_success:
                LOGGER.info(f"Uploaded {file_path} to Dropbox as {dropbox_path}")
            else:
                LOGGER.warning(f"Failed to upload {file_path} to Dropbox.")

        except Exception as ex:
            LOGGER.error(f"Error uploading {file_path} to Dropbox: {ex}")


    async def cleanup_local_files(self, files_to_delete):
        """
        Deletes the uploaded files from local storage.
        """
        for file_path in files_to_delete:
            try:
                os.remove(file_path)
                LOGGER.info(f"Deleted local file: {file_path}")
            except Exception as ex:
                LOGGER.warning(f"Failed to delete {file_path}: {ex}")


    async def update_project_status(self):
        """
        Update the project status in the database to mark it as synced.
        """
        try:
            query = "UPDATE projects SET is_synced = TRUE WHERE is_synced = FALSE"
            with self.db_conn as db:
                db.execute_query(query)
            LOGGER.info("Project status updated in database.")
        except Exception as ex:
            LOGGER.error(f"Failed to update project status in database: {ex}")


if __name__ == "__main__":
    """
    Start the Async File Manager to scan and sync files.
    """
    manager = AsyncFileManager()
    asyncio.run(manager.scan_and_sync())
