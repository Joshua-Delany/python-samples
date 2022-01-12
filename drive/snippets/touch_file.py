

def touch_file():
    drive_service = self.service
    # [START touchFile]
    file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
    file_metadata = {
        'modifiedTime': datetime.utcnow().isoformat() + 'Z'
    }
    # [START_EXCLUDE silent]
    file_id = real_file_id
    file_metadata['modifiedTime'] = real_timestamp
    # [END_EXCLUDE]
    file = drive_service.files().update(fileId=file_id,
                                        body=file_metadata,
                                        fields='id, modifiedTime').execute()
    print
    'Modified time: %s' % file.get('modifiedTime')
    # [END touchFile]
    return file.get('modifiedTime')
