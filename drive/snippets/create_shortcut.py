def create_shortcut(self):
    drive_service = self.service
    # [START createShortcut]
    file_metadata = {
        'title': 'Project plan',
        'mimeType': 'application/vnd.google-apps.drive-sdk'
    }
    file = drive_service.files().insert(body=file_metadata,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END createShortcut]
    return file.get('id')
