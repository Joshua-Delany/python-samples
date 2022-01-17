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


def upload_to_folder():
    drive_service = self.service
    # [START uploadToFolder]
    folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
    # [START_EXCLUDE silent]
    folder_id = real_folder_id
    # [END_EXCLUDE]
    file_metadata = {
        'name': 'photo.jpg',
        'parents': [folder_id]
    }
    media = MediaFileUpload('files/photo.jpg',
                            mimetype='image/jpeg',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: {file_id}'.format(file_id=file.get('id')))
    # [END uploadToFolder]
    return file.get('id')
