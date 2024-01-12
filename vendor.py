#!/usr/bin/env python

from buyrite.validation.base import ValidatorABC


class VendorValidator(ValidatorABC):

    def __init__(self):
        super().__init__()

    def validate_vendor(self, req_data):
        keys = [ 'code', 'name', 'address', 'phone_number', 'sales_representative', 'sales_contact_phone_number', 'sales_contact_email', 'procurement_email', 'last_updated_date', 'last_updated_by']
        return self.perform_common_validations(keys, req_data)

