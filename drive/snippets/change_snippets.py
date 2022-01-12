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

import simplejson
import io
from datetime import datetime
from apiclient import errors


def fetch_start_page_token(drive_service):
    # [START fetchStartPageToken]
    response = drive_service.changes().getStartPageToken().execute()
    print
    'Start token: %s' % response.get('startPageToken')
    # [END fetchStartPageToken]
    return response.get('startPageToken')


def fetch_changes(drive_service, saved_start_page_token):
    # [START fetchChanges]
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
    # [END fetchChanges]
    return saved_start_page_token
