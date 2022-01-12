

def create_shortcut():
    drive_service = self.service
    # [START createShortcut]
    file_metadata = {
        'name': 'Project plan',
        'mimeType': 'application/vnd.google-apps.drive-sdk'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END createShortcut]
    return file.get('id')
