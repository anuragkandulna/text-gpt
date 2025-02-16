import dropbox
import sys
from dropbox.exceptions import ApiError, AuthError
from utils.custom_logger import CustomLogger

# Dropbox access token secret (Replace with your actual token)
TOKEN = ''

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class DropboxConnect:
    def __init__(self) -> None:
        """
        Setup a connection object to Dropbox.
        """
        try:
            if not TOKEN:
                raise ValueError("Dropbox Access Token is missing.")

            # Initialize Dropbox client
            self.dbx = dropbox.Dropbox(TOKEN)

            # Verify authentication
            self._check_authentication()

        except AuthError as auth_err:
            LOGGER.critical(f"Authentication failed: {auth_err}")
            sys.exit(1)
        except Exception as ex:
            LOGGER.critical(f"Failed to connect to Dropbox: {ex}")
            sys.exit(1)

    def _check_authentication(self):
        """
        Check if authentication to Dropbox is successful.
        """
        try:
            account_info = self.dbx.users_get_current_account()
            LOGGER.info(f"Connected to Dropbox as: {account_info.name.display_name}")
        except AuthError:
            raise AuthError("Invalid Dropbox Access Token. Authentication failed.")

    def __enter__(self):
        """
        Enter runtime context related to this connection object.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit runtime context related to this object.
        """
        LOGGER.info("Dropbox connection closed.")

    def check_space_usage(self):
        """
        Retrieve Dropbox account space usage.
        """
        try:
            space_usage = self.dbx.users_get_space_usage()
            LOGGER.info(f"Used: {space_usage.used / (1024 ** 3):.2f} GB, "
                        f"Allocated: {space_usage.allocation.get_individual().allocated / (1024 ** 3):.2f} GB")
            return space_usage
        except ApiError as api_err:
            LOGGER.error(f"Failed to fetch space usage: {api_err}")
            return None


# Example usage
if __name__ == "__main__":
    with DropboxConnect() as dropbox_client:
        dropbox_client.check_space_usage()