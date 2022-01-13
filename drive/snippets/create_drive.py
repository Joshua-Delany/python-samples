# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
