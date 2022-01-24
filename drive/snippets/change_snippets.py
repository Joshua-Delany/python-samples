import simplejson
import io
from datetime import datetime
from apiclient import errors
class ChangeSnippets:
    def __init__(self, service):
        self.service = service
    def fetch_start_page_token(self):
        drive_service = self.service
        # [START fetchStartPageToken]
        response = drive_service.changes().getStartPageToken().execute()
        print 'Start token: %s' % response.get('startPageToken')
        # [END fetchStartPageToken]
        return response.get('startPageToken')
    def fetch_changes(self, saved_start_page_token):
        drive_service = self.service
        # [START fetchChanges]
        # Begin with our last saved start token for this user or the
        # current token from getStartPageToken()
        page_token = saved_start_page_token
        while page_token is not None:
            response = drive_service.changes().list(pageToken=page_token,
                                                    spaces='drive').execute()
            for change in response.get('items'):
                # Process change
                print 'Change found for file: %s' % change.get('fileId')
            if 'newStartPageToken' in response:
                # Last page, save this token for the next polling interval
                saved_start_page_token = response.get('newStartPageToken')
            page_token = response.get('nextPageToken')
        # [END fetchChanges]
        return saved_start_page_token
