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


def upload_app_data(self):
    drive_service = self.service
    # [START uploadAppData]
    file_metadata = {
        'name': 'config.json',
        'parents': ['appDataFolder']
    }
    media = MediaFileUpload('files/config.json',
                            mimetype='application/json',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
    # [END uploadAppData]
    return file.get('id')
