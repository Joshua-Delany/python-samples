

def export_pdf():
    drive_service = self.service
    # [START exportPdf]
    file_id = '1ZdR3L3qP4Bkq8noWLJHSr_iBau0DNT4Kli4SxNc2YEo'
    # [START_EXCLUDE silent]
    file_id = real_file_id
    # [END_EXCLUDE]
    request = drive_service.files().export_media(fileId=file_id,
                                                 mimeType='application/pdf')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print
        "Download %d%%." % int(status.progress() * 100)
    # [END exportPdf]
    return fh.getvalue()
