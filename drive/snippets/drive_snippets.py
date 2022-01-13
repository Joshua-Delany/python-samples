import simplejson
import io
import uuid
from datetime import datetime
from apiclient import errors
class DriveSnippets:
    def __init__(self, service):
        self.service = service
    def create_drive(self):
        drive_service = self.service
        # [START createDrive]
        drive_metadata = {'name': 'Project Resources'}
        request_id = str(uuid.uuid4())
        drive = drive_service.drives().create(body=drive_metadata,
                                                       requestId=request_id,
                                                       fields='id').execute()
        print 'Drive ID: %s' % drive.get('id')
        # [END createDrive]
        return drive.get('id')
    def recover_drives(self, real_user):
        drive_service = self.service
        drives = []
        # [START recoverDrives]
        # Find all shared drives without an organizer and add one.
        # Note: This example does not capture all cases. Shared drives
        # that have an empty group as the sole organizer, or an
        # organizer outside the organization are not captured. A
        # more exhaustive approach would evaluate each shared drive
        # and the associated permissions and groups to ensure an active
        # organizer is assigned.
        page_token = None
        new_organizer_permission = {
            'type': 'user',
            'role': 'organizer',
            'emailAddress': 'user@example.com'
        }
        # [START_EXCLUDE silent]
        new_organizer_permission['emailAddress'] = real_user
        # [END_EXCLUDE]
        while True:
            response = drive_service.drives().list(
                    q='organizerCount = 0',
                    fields='nextPageToken, drives(id, name)',
                    useDomainAdminAccess = True,
                    pageToken=page_token).execute()
            for drive in response.get('drives', []):
                print 'Found shared drive without organizer: %s (%s)' % (
                    drive.get('title'), drive.get('id'))
                permission = drive_service.permissions().create(
                        fileId=drive.get('id'),
                        body=new_organizer_permission,
                        useDomainAdminAccess = True,
                        supportsAllDrives = True,
                        fields='id').execute()
                print 'Added organizer permission: %s ' % (permission.get('id'))
            # [START_EXCLUDE silent]
            drives.extend(response.get('drives', []))
            # [END_EXCLUDE]
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        # [END recoverDrives]
        return drives
