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


def recover_drives():
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    try:
        drive_service = build('drive', 'v3', credentials=creds)
        drives = []
        # [START recoverDrives]
        # Find all shared drives without an organizer and add one.
        # Note: This example does not capture all cases. Shared drives
        # that have an empty group as the sole organizer, or an
        # organizer outside the organization are not captured. A
        # more exhaustive approach would evaluate each shared drive
        # and the associated permissions and groups to ensure an active
        # organizer is assigned.
        page_token = None
        new_organizer_permission = {
            'type': 'user',
            'role': 'organizer',
            'emailAddress': 'user@example.com'
        }
        # [START_EXCLUDE silent]
        new_organizer_permission['emailAddress'] = real_user
        # [END_EXCLUDE]
        while True:
            response = drive_service.drives().list(
                q='organizerCount = 0',
                fields='nextPageToken, drives(id, name)',
                useDomainAdminAccess=True,
                pageToken=page_token).execute()
            for drive in response.get('drives', []):
                print
                'Found shared drive without organizer: %s (%s)' % (
                    drive.get('title'), drive.get('id'))
                permission = drive_service.permissions().create(
                    fileId=drive.get('id'),
                    body=new_organizer_permission,
                    useDomainAdminAccess=True,
                    supportsAllDrives=True,
                    fields='id').execute()
                print
                'Added organizer permission: %s ' % (permission.get('id'))
            # [START_EXCLUDE silent]
            drives.extend(response.get('drives', []))
            # [END_EXCLUDE]
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        # [END recoverDrives]
        return drives
    except HttpError as err:
            # TODO(developer) - handle error appropriately
            print('An error occurred: {error}'.format(error=err))
            raise


if __name__ == '__main__':
    recover_drives()
