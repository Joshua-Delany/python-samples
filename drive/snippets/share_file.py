

def share_file():
    drive_service = self.service
    ids = []
    # [START shareFile]
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    # [START_EXCLUDE silent]
    file_id = real_file_id

    # [END_EXCLUDE]
    def callback(request_id, response, exception):
        if exception:
            # Handle error
            print
            exception
        else:
            print
            "Permission Id: %s" % response.get('id')
            # [START_EXCLUDE silent]
            ids.append(response.get('id'))
            # [END_EXCLUDE]

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
    # [END shareFile]
    return ids