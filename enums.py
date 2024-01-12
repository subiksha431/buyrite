#!/usr/bin/env python

from buyrite.api.model.base import ApiModelABC


class CaseStatus(Enum):
    OPEN = 'open'


class InvoiceStatus(Enum):
    CREATED = 'c'
