import os
import json
import requests
import dropbox
from dropbox.exceptions import AuthError
from utils.custom_logger import CustomLogger

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()

# Dropbox App Credentials (Replace with your actual credentials)
APP_KEY = "f3zpj1mg7wuos1s"
APP_SECRET = "8o1ebj1wiucq6bk"
REFRESH_TOKEN = ""

# Token file to store & reuse access tokens
TOKEN_FILE = "dropbox_token.json"


class DropboxConnect:
    def __init__(self):
        """
        Setup a connection object and handle token authentication.
        """
        self.access_token = self._load_access_token()
        if not self.access_token:
            LOGGER.warning("No valid Dropbox token found. Refreshing...")
            self.access_token = self._refresh_access_token()

        if not self.access_token:
            LOGGER.critical("Failed to obtain a valid Dropbox token.")
            raise AuthError("Invalid Dropbox Token.")

        self.dbx = dropbox.Dropbox(self.access_token)
        self._check_authentication()

    def _load_access_token(self):
        """
        Load the saved access token from a file.
        """
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as file:
                data = json.load(file)
                return data.get("access_token", None)
        return None

    def _save_access_token(self, token):
        """
        Save the new access token to a file.
        """
        with open(TOKEN_FILE, "w") as file:
            json.dump({"access_token": token}, file)
        LOGGER.info("New Dropbox access token saved successfully.")

    def _refresh_access_token(self):
        """
        Refresh the Dropbox access token using the refresh token.
        """
        if not REFRESH_TOKEN:
            LOGGER.critical("No Dropbox refresh token found. Please generate one.")
            return None  # Prevent invalid API requests

        url = "https://api.dropbox.com/oauth2/token"
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": APP_KEY,
            "client_secret": APP_SECRET,
        }

        LOGGER.info(f"Refreshing token with payload: {payload}")  # Debugging

        try:
            response = requests.post(url, data=payload)
            if response.status_code != 200:
                LOGGER.critical(f"Token refresh failed: {response.status_code}, {response.text}")  # Log exact error
                return None

            data = response.json()
            new_access_token = data["access_token"]
            self._save_access_token(new_access_token)
            LOGGER.info("Dropbox access token refreshed successfully.")
            return new_access_token
        except requests.exceptions.RequestException as ex:
            LOGGER.critical(f"Failed to refresh Dropbox access token: {ex}")
            return None

    def _check_authentication(self):
        """
        Verify Dropbox authentication.
        """
        try:
            account_info = self.dbx.users_get_current_account()
            LOGGER.info(f"Connected to Dropbox as: {account_info.name.display_name}")
        except AuthError:
            LOGGER.critical("Dropbox authentication failed.")
            raise AuthError(None, "Invalid Dropbox Access Token.")

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