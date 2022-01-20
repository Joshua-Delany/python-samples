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
    print
    'File ID: %s' % file.get('id')
    # [END uploadAppData]
    return file.get('id')
