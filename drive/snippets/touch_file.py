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
    print
    'Modified time: %s' % file.get('modifiedDate')
    # [END touchFile]
    return file.get('modifiedDate')
