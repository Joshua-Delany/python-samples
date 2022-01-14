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

# [START drive_create_drive]
import uuid

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth


def create_drive():
    """Creates a new shared drive

    Returns:
        The id of the newly created shared drive in dictionary format.
    """
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        # Create the drive v3 API client
        drive_service = build('drive', 'v3', credentials=creds)

        # Build and execute request to create a new shared drive
        drive_metadata = {'name': 'Project Resources'}
        request_id = str(uuid.uuid4())
        drive = drive_service.drives().create(body=drive_metadata,
                                              requestId=request_id,
                                              fields='id').execute()

        print('Drive ID: {drive_id}'.format(drive_id=drive.get('id')))
        return drive.get('id')
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_create_drive]


if __name__ == '__main__':
    create_drive()