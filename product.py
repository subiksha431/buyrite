#!/usr/bin/env python

from buyrite.validation.base import ValidatorABC


class ProductValidator(ValidatorABC):

    def __init__(self):
        super().__init__()

    def validate_product(self, req_data):
        keys = [ 'item', 'description', 'type', 'unit_price', 'unit_markup', 'sale_price', 'units_in_carton', 'carton_price', 'sold_as_carton', 'sale_unit', 'unit_size', 'last_updated_date', 'last_updated_by']
        return self.perform_common_validations(keys, req_data)

class ProductSalesValidator(ValidatorABC):

    def __init__(self):
        super().__init__()

    def validate_product_sales(self, req_data):
        keys = [ 'product_id', 'sales_from_date', 'sales_end_date', 'units_sold', 'units_discount_price']
        return self.perform_common_validations(keys, req_data)
