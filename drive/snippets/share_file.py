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

# [START drive_share_file]
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth


def share_file():
    # Load pre-authorized user credentials from the environment.
    # TODO(developer) - See https://developers.google.com/identity for
    # guides on implementing OAuth2 for your application.
    creds, _ = google.auth.default()

    ids = []
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    # [START_EXCLUDE silent]
    file_id = real_file_id

    # [END_EXCLUDE]
    def callback(request_id, response, exception):
        if exception:
            # Handle error
            print('An error occurred: {exception}'.format(exception=exception))
        else:
            print('Permission Id: {id}'.format(id=response.get('id')))
            # [START_EXCLUDE silent]
            ids.append(response.get('id'))
            # [END_EXCLUDE]

    try:
        drive_service = build('drive', 'v3', credentials=creds)
        batch = drive_service.new_batch_http_request(callback=callback)
        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': 'user@example.com'
        }
        # [START_EXCLUDE silent]
        user_permission['emailAddress'] = real_user
        # [END_EXCLUDE]
        batch.add(drive_service.permissions().create(
            fileId=file_id,
            body=user_permission,
            fields='id',
        ))
        domain_permission = {
            'type': 'domain',
            'role': 'reader',
            'domain': 'example.com'
        }
        # [START_EXCLUDE silent]
        domain_permission['domain'] = real_domain
        # [END_EXCLUDE]
        batch.add(drive_service.permissions().create(
            fileId=file_id,
            body=domain_permission,
            fields='id',
        ))
        batch.execute()
        return ids
    except HttpError as err:
        # TODO(developer) - handle error appropriately
        print('An error occurred: {error}'.format(error=err))
        raise
# [END drive_share_file]
