import dropbox
import sys
from dropbox.exceptions import ApiError, AuthError

TOKEN = 'TOKEN'


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
