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


def download_file():
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    drive_service = build('drive', 'v2', credentials=creds)
    # [START downloadFile]
    file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print('Download {status}%.'.format(status=int(status.progress() * 100)))
    # [END downloadFile]
    return fh.getvalue()
