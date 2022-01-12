import simplejson
import io
from datetime import datetime
from apiclient import errors


def fetch_start_page_token(drive_service):
    # [START fetchStartPageToken]
    response = drive_service.changes().getStartPageToken().execute()
    print
    'Start token: %s' % response.get('startPageToken')
    # [END fetchStartPageToken]
    return response.get('startPageToken')


def fetch_changes(drive_service, saved_start_page_token):
    # [START fetchChanges]
    # Begin with our last saved start token for this user or the
    # current token from getStartPageToken()
    page_token = saved_start_page_token
    while page_token is not None:
        response = drive_service.changes().list(pageToken=page_token,
                                                spaces='drive').execute()
        for change in response.get('changes'):
            # Process change
            print
            'Change found for file: %s' % change.get('fileId')
        if 'newStartPageToken' in response:
            # Last page, save this token for the next polling interval
            saved_start_page_token = response.get('newStartPageToken')
        page_token = response.get('nextPageToken')
    # [END fetchChanges]
    return saved_start_page_token
