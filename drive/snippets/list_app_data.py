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


def list_app_data(self):
    drive_service = self.service
    # [START listAppData]
    response = drive_service.files().list(spaces='appDataFolder',
                                          fields='nextPageToken, items(id, title)',
                                          maxResults=10).execute()
    for file in response.get('items', []):
        # Process change
        print('Found file: {file_name} ({file_id})'.format(
            file_name=file.get('title'), file_id=file.get('id')))
    # [END listAppData]
    return response.get('items')
