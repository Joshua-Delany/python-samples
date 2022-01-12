

def upload_to_folder():
    drive_service = self.service
    # [START uploadToFolder]
    folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
    # [START_EXCLUDE silent]
    folder_id = real_folder_id
    # [END_EXCLUDE]
    file_metadata = {
        'name': 'photo.jpg',
        'parents': [folder_id]
    }
    media = MediaFileUpload('files/photo.jpg',
                            mimetype='image/jpeg',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END uploadToFolder]
    return file.get('id')
