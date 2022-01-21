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


def touch_file(self, real_file_id, real_timestamp):
    drive_service = self.service
    # [START touchFile]
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    file_metadata = {
        'modifiedDate': datetime.utcnow().isoformat() + 'Z'
    }
    # [START_EXCLUDE silent]
    file_id = real_file_id
    file_metadata['modifiedDate'] = real_timestamp
    # [END_EXCLUDE]
    file = drive_service.files().update(fileId=file_id,
                                        body=file_metadata,
                                        setModifiedDate=True,
                                        fields='id, modifiedDate').execute()
    print('Modified time: {update_time}'.format(
        update_time=file.get('modifiedDate')))
    # [END touchFile]
    return file.get('modifiedDate')
