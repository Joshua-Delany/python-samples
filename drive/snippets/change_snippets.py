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
from googleapiclient.errors import HttpError
import google.auth


# [START drive_fetch_start_page_token]
def fetch_start_page_token(drive_service):
    try:
        response = drive_service.changes().getStartPageToken().execute()
        print
        'Start token: %s' % response.get('startPageToken')
        return response.get('startPageToken')
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_fetch_start_page_token]


# [START drive_fetch_changes]
def fetch_changes(drive_service, saved_start_page_token):
    try:
        # Begin with our last saved start token for this user or the
        # current token from getStartPageToken()
        page_token = saved_start_page_token
        while page_token is not None:
            response = drive_service.changes().list(pageToken=page_token,
                                                    spaces='drive').execute()
            for change in response.get('changes'):
                # Process change
                print
                'Change found for file: %s' % change.get('fileId')
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


def main():
    """Demonstrates usage of fetch_start_page_token and fetch_changes
    """
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        # Create the drive v3 API client
        drive_service = build('drive', 'v3', credentials=creds)

        # Fetch a page token
        start_page_token = fetch_start_page_token(drive_service=drive_service)

        # Build and execute request to create a new folder.
        file_metadata = {
            'name': 'Invoices',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        drive_service.files().create(body=file_metadata, fields='id').execute()

        # Check for changes since page token was retrieved
        fetch_changes(drive_service=drive_service,
                      saved_start_page_token=start_page_token)
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise


if __name__ = '__main__':
    main()
