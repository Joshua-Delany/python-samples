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

from googleapiclient.discovery import build
import google.auth


def create_shortcut():
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    drive_service = build('drive', 'v3', credentials=creds)
    # [START createShortcut]
    file_metadata = {
        'name': 'Project plan',
        'mimeType': 'application/vnd.google-apps.drive-sdk'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END createShortcut]
    return file.get('id')
