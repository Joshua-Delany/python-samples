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

# [START drive_list_app_data]
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth

def list_app_data(self):
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        drive_service = build('drive', 'v3', credentials=creds)
        response = drive_service.files().list(spaces='appDataFolder',
                                              fields='nextPageToken, files(id, name)',
                                              pageSize=10).execute()
        for file in response.get('files', []):
            # Process change
            print('Found file: {file_name} ({file_id})'.format(
                file_name=file.get('name'), file_id=file.get('id')))
        return response.get('files')
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_list_app_data]
