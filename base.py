#!/usr/bin/env python

from buyrite.utils.logging import Logger
from buyrite.utils.restutils import StatusCode


class ValidatorABC:

    def __init__(self):
        self.logger = Logger.build_logger()

    def check_input_values(self, value_to_check):
        result = False
        if len(value_to_check.strip()) != 0:
            result = True
        return result

    def perform_common_validations(self, expected_keys, req_data):
        missing_keys_list = []

        for key in expected_keys:
            if key not in req_data:
                self.logger.info('Adding Key[%s] to missing keyList.', key)
                missing_keys_list.append(key)

        if len(missing_keys_list) == 0:
            self.logger.debug('Validation passed')
            return StatusCode.OK, missing_keys_list

        else:
            self.logger.error('Request will be rejected because required input elements[%s] are not present', missing_keys_list)
            # errorMessage = 'Required input elements for this action ['+str(missing_keys_list)+'] is not present'
            # errorMessage = missing_keys_list
            return StatusCode.UNPROCESSABLE_ENTITY, missing_keys_list
            # raise ApiInputException(errorMessage)

    # TODO - is this required?
    ##### def check_file_values(self, file, invoicesfile_name):
    #####     return StatusCode.BAD_REQUEST if invoicesfile_name not in file else StatusCode.OK
    ##### 
    ##### def check_filename_values(self, file):
    #####     return StatusCode.BAD_REQUEST if file.filename == '' else StatusCode.OK
    ##### 
    ##### def validate_put_upload_file(self, filename):
    #####     return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions
    ##### 
    ##### def check_allowedfile_values(self, file):
    #####     return StatusCode.OK if file and self.validate_put_upload_file(file) else StatusCode.BAD_REQUEST
