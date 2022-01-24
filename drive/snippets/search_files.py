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

# [START drive_search_files]
from googleapiclient.discovery import build
import google.auth


def search_files(self):
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    drive_service = build('drive', 'v2', credentials=creds)
    files = []
    page_token = None
    while True:
        response = drive_service.files().list(q="mimeType='image/jpeg'",
                                              spaces='drive',
                                              fields='nextPageToken, items(id, title)',
                                              pageToken=page_token).execute()
        for file in response.get('items', []):
            # Process change
            print('Found file: {file_name} ({file_id})'.format(
                file_name=file.get('title'), file_id=file.get('id')))
        files.extend(response.get('items', []))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return files
# [END drive_search_files]
