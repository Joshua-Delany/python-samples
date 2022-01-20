import simplejson
import io
from datetime import datetime
from apiclient import errors
from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload
class FileSnippets:
    def __init__(self, service):
        self.service = service

    def upload_basic(self):
        drive_service = self.service
        # [START uploadBasic]
        file_metadata = {'title': 'photo.jpg'}
        media = MediaFileUpload('files/photo.jpg',
                                mimetype='image/jpeg')
        file = drive_service.files().insert(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print 'File ID: %s' % file.get('id')
        # [END uploadBasic]
        return file.get('id')

    def upload_revision(self, real_file_id):
        drive_service = self.service
        # [START uploadRevision]
        file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
        # [START_EXCLUDE silent]
        file_id = real_file_id
        # [END_EXCLUDE]
        media = MediaFileUpload('files/photo.jpg',
                                mimetype='image/jpeg',
                                resumable=True)
        file = drive_service.files().update(fileId=file_id,
                                            body={},
                                            media_body=media,
                                            fields='id').execute()
        print 'File ID: %s' % file.get('id')
        # [END uploadRevision]
        return file.get('id')

    def upload_to_folder(self, real_folder_id):
        drive_service = self.service
        # [START uploadToFolder]
        folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
        # [START_EXCLUDE silent]
        folder_id = real_folder_id
        # [END_EXCLUDE]
        file_metadata = {
            'title': 'photo.jpg',
            'parents': [{'id': folder_id}]
        }
        media = MediaFileUpload('files/photo.jpg',
                                mimetype='image/jpeg',
                                resumable=True)
        file = drive_service.files().insert(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print 'File ID: %s' % file.get('id')
        # [END uploadToFolder]
        return file.get('id')

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
        print 'File ID: %s' % file.get('id')
        # [END uploadWithConversion]
        return file.get('id')

    def export_pdf(self, real_file_id):
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
            print "Download %d%%." % int(status.progress() * 100)
        # [END exportPdf]
        return fh.getvalue()

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
            print "Download %d%%." % int(status.progress() * 100)
        # [END downloadFile]
        return fh.getvalue()

    def create_shortcut(self):
        drive_service = self.service
        # [START createShortcut]
        file_metadata = {
            'title': 'Project plan',
            'mimeType': 'application/vnd.google-apps.drive-sdk'
        }
        file = drive_service.files().insert(body=file_metadata,
                                            fields='id').execute()
        print 'File ID: %s' % file.get('id')
        # [END createShortcut]
        return file.get('id')

    def touch_file(self, real_file_id, real_timestamp):
        drive_service = self.service
        # [START touchFile]
        file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
        file_metadata = {
            'modifiedDate': datetime.utcnow().isoformat() + 'Z'
        }
        # [START_EXCLUDE silent]
        file_id = real_file_id
        file_metadata['modifiedDate'] = real_timestamp
        # [END_EXCLUDE]
        file = drive_service.files().update(fileId=file_id,
                                            body=file_metadata,
                                            setModifiedDate=True,
                                            fields='id, modifiedDate').execute()
        print 'Modified time: %s' % file.get('modifiedDate')
        # [END touchFile]
        return file.get('modifiedDate')

    def create_folder(self):
        drive_service = self.service
        # [START createFolder]
        file_metadata = {
            'title': 'Invoices',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = drive_service.files().insert(body=file_metadata,
                                            fields='id').execute()
        print 'Folder ID: %s' % file.get('id')
        # [END createFolder]
        return file.get('id')

    def move_file_to_folder(self, real_file_id, real_folder_id):
        drive_service = self.service
        # [START moveFileToFolder]
        file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
        folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
        # [START_EXCLUDE silent]
        file_id = real_file_id
        folder_id = real_folder_id
        # [END_EXCLUDE]
        # Retrieve the existing parents to remove
        file = drive_service.files().get(fileId=file_id,
                                         fields='parents').execute()
        previous_parents = ",".join([parent["id"] for parent in file.get('parents')])
        # Move the file to the new folder
        file = drive_service.files().update(fileId=file_id,
                                            addParents=folder_id,
                                            removeParents=previous_parents,
                                            fields='id, parents').execute()
        # [END moveFileToFolder]
        return [parent["id"] for parent in file.get('parents')]

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
                print 'Found file: %s (%s)' % (file.get('title'), file.get('id'))
            # [START_EXCLUDE silent]
            files.extend(response.get('items', []))
            # [END_EXCLUDE]
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        # [END searchFiles]
        return files

    def share_file(self, real_file_id, real_user, real_domain):
        drive_service = self.service
        ids = []
        # [START shareFile]
        file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
        # [START_EXCLUDE silent]
        file_id = real_file_id
        # [END_EXCLUDE]
        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print exception
            else:
                print "Permission Id: %s" % response.get('id')
                # [START_EXCLUDE silent]
                ids.append(response.get('id'))
                # [END_EXCLUDE]
        batch = drive_service.new_batch_http_request(callback=callback)
        user_permission = {
            'type': 'user',
            'role': 'writer',
            'value': 'user@example.com'
        }
        # [START_EXCLUDE silent]
        user_permission['value'] = real_user
        # [END_EXCLUDE]
        batch.add(drive_service.permissions().insert(
                fileId=file_id,
                body=user_permission,
                fields='id',
        ))
        domain_permission = {
            'type': 'domain',
            'role': 'reader',
            'value': 'example.com'
        }
        # [START_EXCLUDE silent]
        domain_permission['value'] = real_domain
        # [END_EXCLUDE]
        batch.add(drive_service.permissions().insert(
                fileId=file_id,
                body=domain_permission,
                fields='id',
        ))
        batch.execute()
        # [END shareFile]
        return ids