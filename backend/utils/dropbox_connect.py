import os
import json
import requests
import webbrowser
import dropbox
from dropbox.exceptions import AuthError
from variables import DBX_APP_KEY, DBX_APP_SECRET, DBX_TOKEN_FILE
from utils.custom_logger import CustomLogger

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class DropboxConnect:
    def __init__(self):
        """
        Setup Dropbox OAuth connection and handle token authentication.
        """
        self.auth_url = f"https://www.dropbox.com/oauth2/authorize?client_id={DBX_APP_KEY}&response_type=code&token_access_type=offline"
        self.access_token = None
        self.refresh_token = self._load_refresh_token()

        if not self.refresh_token:
            LOGGER.warning("No refresh token found. Starting OAuth flow...")
            self.refresh_token = self._get_refresh_token()

        if not self.refresh_token:
            LOGGER.critical("Failed to obtain a valid Dropbox refresh token.")
            raise AuthError(None, "Invalid Dropbox Refresh Token.")

        self.access_token = self._refresh_access_token()
        self.dbx = dropbox.Dropbox(self.access_token)
        self._check_authentication()

    def _load_refresh_token(self):
        """
        Load the saved refresh token from a file.
        """
        if os.path.exists(DBX_TOKEN_FILE):
            with open(DBX_TOKEN_FILE, "r") as file:
                data = json.load(file)
                return data.get("refresh_token", None)
        return None

    def _save_refresh_token(self, refresh_token):
        """
        Save the new refresh token to a file.
        """
        with open(DBX_TOKEN_FILE, "w") as file:
            json.dump({"refresh_token": refresh_token}, file)
        LOGGER.info("Dropbox refresh token saved successfully.")

    def _get_refresh_token(self):
        """
        Get a new refresh token by completing the OAuth flow.
        """
        LOGGER.info("Opening Dropbox OAuth authorization URL...")
        webbrowser.open(self.auth_url)

        auth_code = input("Enter the authorization code from Dropbox: ").strip()
        url = "https://api.dropbox.com/oauth2/token"
        payload = {
            "code": auth_code,
            "grant_type": "authorization_code",
            "client_id": DBX_APP_KEY,
            "client_secret": DBX_APP_SECRET,
        }
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            data = response.json()
            refresh_token = data.get("refresh_token")

            if refresh_token:
                self._save_refresh_token(refresh_token)
                LOGGER.info("Dropbox OAuth flow completed successfully.")
                return refresh_token

        except requests.exceptions.RequestException as ex:
            LOGGER.critical(f"Failed to obtain refresh token: {ex}")
            return None

    def _refresh_access_token(self):
        """
        Refresh the Dropbox access token using the refresh token.
        """
        if not self.refresh_token:
            LOGGER.critical("No Dropbox refresh token found. Cannot refresh access token.")
            return None

        url = "https://api.dropbox.com/oauth2/token"
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": DBX_APP_KEY,
            "client_secret": DBX_APP_SECRET,
        }

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            data = response.json()
            new_access_token = data["access_token"]
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
