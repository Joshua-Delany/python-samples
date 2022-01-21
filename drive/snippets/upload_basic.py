def upload_basic(self):
    drive_service = self.service
    # [START uploadBasic]
    file_metadata = {'title': 'photo.jpg'}
    media = MediaFileUpload('files/photo.jpg',
                            mimetype='image/jpeg')
    file = drive_service.files().insert(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END uploadBasic]
    return file.get('id')
