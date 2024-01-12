#!/usr/bin/env python

from buyrite.validation.base import ValidatorABC


class StoreValidator(ValidatorABC):

    def __init__(self):
        super().__init__()

    def validate_store(self, req_data):
        keys = ['location', 'type', 'owner', 'rent', 'rent_payment_window']
        return self.perform_common_validations(keys, req_data)

    def validate_store_update(self, req_data):
        keys = ['store_id', 'email', 'role', 'title', 'working_hours', 'hourly_rate','weekly_payment','hire_date','termination_date']
        return self.perform_common_validations(keys, req_data)
