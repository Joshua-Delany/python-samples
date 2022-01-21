def download_file(self, real_file_id):
    drive_service = self.service
    # [START downloadFile]
    file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    # [START_EXCLUDE silent]
    file_id = real_file_id
    # [END_EXCLUDE]
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print
        "Download %d%%." % int(status.progress() * 100)
    # [END downloadFile]
    return fh.getvalue()
