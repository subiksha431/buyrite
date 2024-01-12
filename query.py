#!/usr/bin/env python


class AnalysisQueryParameters:

    def __init__(self, offset=None, limit=None, store_id=None, product_id=None, product_type=None):
        self.offset = 0 if offset is None else int(offset)
        self.limit = 50 if limit is None else int(limit)
        self.store_id = store_id if store_id is None else str(store_id)
        self.product_id = product_id if product_id is None else str(product_id)
        self.product_type = product_type if product_type is None else str(product_type)
