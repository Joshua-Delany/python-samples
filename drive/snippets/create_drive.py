import simplejson
import io
import uuid
from datetime import datetime
from apiclient import errors

def create_drive(self):
    drive_service = self.service
    # [START createDrive]
    drive_metadata = {'name': 'Project Resources'}
    request_id = str(uuid.uuid4())
    drive = drive_service.drives().create(body=drive_metadata,
                                          requestId=request_id,
                                          fields='id').execute()
    print
    'Drive ID: %s' % drive.get('id')
    # [END createDrive]
    return drive.get('id')
