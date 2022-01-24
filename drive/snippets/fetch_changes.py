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

# [START drive_fetch_changes]
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth


def fetch_changes(saved_start_page_token):
    """Fetches changes made since passed page token was created

    Args:
        saved_start_page_token: A page token

    Returns:
        A new page token
    """
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        # Create the drive v3 API client
        drive_service = build('drive', 'v2', credentials=creds)

        # Check all files in drive space for changes
        page_token = saved_start_page_token
        while page_token is not None:
            response = drive_service.changes().list(pageToken=page_token,
                                                    spaces='drive').execute()
            for change in response.get('items'):
                # Process change
                print('Change found for file: {file_id}'.format(
                    file_id=change.get('fileId')))
            if 'newStartPageToken' in response:
                # Last page, save this token for the next polling interval
                saved_start_page_token = response.get('newStartPageToken')
            page_token = response.get('nextPageToken')
        return saved_start_page_token
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_fetch_changes]
