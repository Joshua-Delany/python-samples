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

from __future__ import print_function

# [START drive_touch_file]
from datetime import datetime

from googleapiclient.discovery import build
import google.auth


def touch_file():
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    drive_service = build('drive', 'v3', credentials=creds)
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    file_metadata = {
        'modifiedTime': datetime.utcnow().isoformat() + 'Z'
    }
    file = drive_service.files().update(fileId=file_id,
                                        body=file_metadata,
                                        fields='id, modifiedTime').execute()
    print('Modified time: {time}'.format(time=file.get('modifiedTime')))
    return file.get('modifiedTime')
# [END drive_touch_file]
