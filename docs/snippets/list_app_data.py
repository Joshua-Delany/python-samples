def list_app_data(self):
    drive_service = self.service
    # [START listAppData]
    response = drive_service.files().list(spaces='appDataFolder',
                                          fields='nextPageToken, files(id, name)',
                                          pageSize=10).execute()
    for file in response.get('files', []):
        # Process change
        print
        'Found file: %s (%s)' % (file.get('name'), file.get('id'))
    # [END listAppData]
    return response.get('files')
