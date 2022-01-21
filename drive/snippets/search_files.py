def search_files(self):
    drive_service = self.service
    files = []
    # [START searchFiles]
    page_token = None
    while True:
        response = drive_service.files().list(q="mimeType='image/jpeg'",
                                              spaces='drive',
                                              fields='nextPageToken, items(id, title)',
                                              pageToken=page_token).execute()
        for file in response.get('items', []):
            # Process change
            print
            'Found file: %s (%s)' % (file.get('title'), file.get('id'))
        # [START_EXCLUDE silent]
        files.extend(response.get('items', []))
        # [END_EXCLUDE]
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    # [END searchFiles]
    return files