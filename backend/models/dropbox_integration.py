import dropbox
import sys
from dropbox.exceptions import ApiError, AuthError


TOKEN = ''


class DropboxIntegration():
    def __init__(self) -> None:
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

    def connect(self):
        """
        Connect to dropbox.
        """



    def register(self, username, user_uuid, ):
        """
        Create a new directory for a user upon new registration.
        """
        pass



if __name__ == '__main__':
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. "
            "Open up backup-and-restore-example.py in a text editor and "
            "paste in your token in line 14.")
    
    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    with dropbox.Dropbox(TOKEN) as dbx:

        # Check that the access token is valid
        try:
            username = dbx.users_get_current_account()
            print(username)
        except AuthError:
            sys.exit("ERROR: Invalid access token; try re-generating an "
                "access token from the app console on the web.")
        
        print('Done!')
