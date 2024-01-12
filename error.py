#!/usr/bin/env python

from datetime import datetime

from buyrite.api.model.base import ApiModelABC
from buyrite.utils.datautils import new_guid


class ErrorApiModel(ApiModelABC):

    def __init__(self, message):
        self.code = new_guid()
        self.message = message
        self.timestamp = datetime.utcnow().isoformat()
