def list_app_data(self):
    drive_service = self.service
    # [START listAppData]
    response = drive_service.files().list(spaces='appDataFolder',
                                          fields='nextPageToken, items(id, title)',
                                          maxResults=10).execute()
    for file in response.get('items', []):
        # Process change
        print
        'Found file: %s (%s)' % (file.get('title'), file.get('id'))
    # [END listAppData]
    return response.get('items')
