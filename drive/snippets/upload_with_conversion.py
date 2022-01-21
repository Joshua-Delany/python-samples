def upload_with_conversion(self):
    drive_service = self.service
    # [START uploadWithConversion]
    file_metadata = {
        'title': 'My Report',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload('files/report.csv',
                            mimetype='text/csv',
                            resumable=True)
    file = drive_service.files().insert(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END uploadWithConversion]
    return file.get('id')