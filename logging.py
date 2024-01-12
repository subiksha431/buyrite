#!/usr/bin/env python

import logging

from buyrite.utils.config import Configuration


class Logger:

    @classmethod
    def build_logger(cls):
        config = Configuration()
        logging.basicConfig(format=config.log_format)

        result = logging.getLogger(__name__)
        result.setLevel(config.log_level)
        return result

    @classmethod
    def handle_exception(cls, ex):
        # traceback.print_exc()
        logger = cls.build_logger()
        logger.exception(ex)
