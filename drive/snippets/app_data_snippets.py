import simplejson
import io
from datetime import datetime
from apiclient import errors
from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload

class AppDataSnippets:
    def __init__(self, service):
        self.service = service

    def upload_app_data(self):
        drive_service = self.service
        # [START uploadAppData]
        file_metadata = {
            'title': 'config.json',
            'parents': [{
                'id': 'appDataFolder'
            }]
        }
        media = MediaFileUpload('files/config.json',
                                mimetype='application/json',
                                resumable=True)
        file = drive_service.files().insert(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print 'File ID: %s' % file.get('id')
        # [END uploadAppData]
        return file.get('id')

    def list_app_data(self):
        drive_service = self.service
        # [START listAppData]
        response = drive_service.files().list(spaces='appDataFolder',
                                              fields='nextPageToken, items(id, title)',
                                              maxResults=10).execute()
        for file in response.get('items', []):
            # Process change
            print 'Found file: %s (%s)' % (file.get('title'), file.get('id'))
        # [END listAppData]
        return response.get('items')

    def fetch_app_data_folder(self):
        drive_service = self.service
        # [START fetchAppDataFolder]
        file = drive_service.files().get(fileId='appDataFolder',
                                         fields='id').execute()
        print 'Folder ID: %s' % file.get('id')
        # [END fetchAppDataFolder]
        return file.get('id')
