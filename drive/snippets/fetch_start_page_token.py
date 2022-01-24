def fetch_start_page_token(self):
    drive_service = self.service
    # [START fetchStartPageToken]
    response = drive_service.changes().getStartPageToken().execute()
    print
    'Start token: %s' % response.get('startPageToken')
    # [END fetchStartPageToken]
    return response.get('startPageToken')
