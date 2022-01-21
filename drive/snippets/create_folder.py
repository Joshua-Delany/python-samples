def create_folder(self):
    drive_service = self.service
    # [START createFolder]
    file_metadata = {
        'title': 'Invoices',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().insert(body=file_metadata,
                                        fields='id').execute()
    print
    'Folder ID: %s' % file.get('id')
    # [END createFolder]
    return file.get('id')
