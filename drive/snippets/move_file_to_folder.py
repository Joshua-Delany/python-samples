

def move_file_to_folder():
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
    previous_parents = ",".join(file.get('parents'))
    # Move the file to the new folder
    file = drive_service.files().update(fileId=file_id,
                                        addParents=folder_id,
                                        removeParents=previous_parents,
                                        fields='id, parents').execute()
    # [END moveFileToFolder]
    return file.get('parents')
