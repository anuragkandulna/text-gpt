from utils.custom_logger import CustomLogger
import dropbox
import sys
from dropbox.exceptions import ApiError, AuthError


# Dropbox access token secret
TOKEN = ''

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class DropboxConnect:
    def __init__(self) -> None:
        """
        Setup a connection object.
        """
        # Check for an access token
        try:
            if (len(TOKEN) == 0):
                raise Exception("Invalid Access Token")
            
            
        
        except Exception as ex:
            LOGGER.critical(f'Failed to connect to dropbox: {ex}')
            raise


    def __enter__(self):
        """
        Enter runtime context related to this connection object.
        """
        pass


    def __exit__(self):
        """
        Exit runtime context related to this object, closing the connection.
        """
        pass
