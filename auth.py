#!/usr/bin/env python

from buyrite.validation.base import ValidatorABC


class AuthValidator(ValidatorABC):

    def __init__(self):
        super().__init__()

    def validate_login_user(self, req_data):
        keys = ['email', 'password']
        return self.perform_common_validations(keys, req_data)

    def validate_header(self, req_data):
        keys = ['Authorization']
        return self.perform_common_validations(keys, req_data)
