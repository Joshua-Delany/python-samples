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

# [START drive_download_file]
import io

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import google.auth


def download_file():
    """Downloads a file

    Returns:
        Contents of the downloaded file
    """
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'

    try:
        # Create the drive v3 API client
        drive_service = build('drive', 'v3', credentials=creds)

        # Build request to download the file
        request = drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()

        # Download file
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print('Download {download_percent}%.'.format(
                download_percent=int(status.progress() * 100)))
        return fh.getvalue()
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_download_file]


if __name__ == '__main__':
    download_file()
