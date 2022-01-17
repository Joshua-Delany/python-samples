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

# [START drive_upload_with_conversion]
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import google.auth


def upload_with_conversion():
    """Uploads a file to the drive space and converts to a workspace filetype.

    Returns:
        Uploaded file's id.
    """
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        # Create the drive v3 API client
        drive_service = build('drive', 'v3', credentials=creds)

        # Create metadata for a sheets file and file upload object for .csv file
        file_metadata = {
            'name': 'My Report',
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        media = MediaFileUpload('files/report.csv',
                                mimetype='text/csv',
                                resumable=True)

        # Upload the .csv file with Google sheets mimeType to convert on upload
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

        print('File ID: {file_id}'.format(file_id=file.get('id')))
        return file.get('id')
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_upload_with_conversion]
