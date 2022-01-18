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
from googleapiclient.errors import HttpError
import google.auth


def search_files():
    """Retrieves and prints the name and id of each jpeg in the drive space.

    Returns:
        List of file ids and names in dictionary format.
    """
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        # Create the drive v3 API client
        drive_service = build('drive', 'v3', credentials=creds)

        files = []
        page_token = None
        while True:
            # Fetch id and name fields of jpeg files in the drive space
            response = drive_service.files().list(q="mimeType='image/jpeg'",
                                                  spaces='drive',
                                                  fields='nextPageToken, files(id, name)',
                                                  pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                print('Found file: {file_name} ({file_id})'.format(
                    file_name=file.get('name'), file_id=file.get('id')))
            files.extend(response.get('files', []))

            # End loop when all files have been retrieved
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return files
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_search_files]


if __name__ == '__main__':
    search_files()
