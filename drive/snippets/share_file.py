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


def share_file(self):
    drive_service = self.service
    ids = []
    # [START shareFile]
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    def callback(request_id, response, exception):
        if exception:
            # Handle error
            print
            exception
        else:
            print
            "Permission Id: %s" % response.get('id')
            ids.append(response.get('id'))

    batch = drive_service.new_batch_http_request(callback=callback)
    user_permission = {
        'type': 'user',
        'role': 'writer',
        'value': 'user@example.com'
    }
    batch.add(drive_service.permissions().insert(
        fileId=file_id,
        body=user_permission,
        fields='id',
    ))
    domain_permission = {
        'type': 'domain',
        'role': 'reader',
        'value': 'example.com'
    }
    batch.add(drive_service.permissions().insert(
        fileId=file_id,
        body=domain_permission,
        fields='id',
    ))
    batch.execute()
    # [END shareFile]
    return ids
