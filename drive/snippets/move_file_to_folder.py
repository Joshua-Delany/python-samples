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


def move_file_to_folder(self, real_file_id, real_folder_id):
    drive_service = self.service
    # [START moveFileToFolder]
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
    # [START_EXCLUDE silent]
    file_id = real_file_id
    folder_id = real_folder_id
    # [END_EXCLUDE]
    # Retrieve the existing parents to remove
    file = drive_service.files().get(fileId=file_id,
                                     fields='parents').execute()
    previous_parents = ",".join([parent["id"] for parent in file.get('parents')])
    # Move the file to the new folder
    file = drive_service.files().update(fileId=file_id,
                                        addParents=folder_id,
                                        removeParents=previous_parents,
                                        fields='id, parents').execute()
    # [END moveFileToFolder]
    return [parent["id"] for parent in file.get('parents')]
