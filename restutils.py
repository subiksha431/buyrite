#!/usr/bin/env python

from enum import IntEnum, unique

import flask

from buyrite.shared.error import ErrorApiModel
from buyrite.utils.jsonutils import JsonSerializer
from buyrite.utils.logging import Logger

logger = Logger.build_logger()


@unique
class StatusCode(IntEnum):
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    UNPROCESSABLE_ENTITY = 422
    SERVER_ERROR = 500

    def is_2xx_successful(self):
        value = int(self)
        return 200 <= value < 300

    def is_4xx_client_error(self):
        value = int(self)
        return 400 <= value < 500

    def is_5xx_server_error(self):
        value = int(self)
        return 500 <= value < 600


class ResponseBuilder:

    @classmethod
    def build_json_response(cls, code, body):
        body = JsonSerializer.serialize(body)
        logger.info('CODE :: %s', code)
        #logger.info('BODY :: %s', body)

        response = flask.make_response(body, int(code))
        response.mimetype = 'application/json'
        return response

    @classmethod
    def build_json_response_with_header(cls, code, body, header):
        body = JsonSerializer.serialize(body)
        logger.info('CODE :: %s', code)
        #logger.info('BODY :: %s', body)

        response = flask.make_response(body, int(code))
        response.mimetype = 'application/json'
        response.headers['r-buyrite-total-rows'] = header
        return response

    @classmethod
    def build_error_response(cls, code: StatusCode, body: ErrorApiModel):
        code = StatusCode.SERVER_ERROR if code is None else code
        body = JsonSerializer.serialize(body)
        logger.info('CODE :: %s', code)
        logger.info('ERROR :: %s', body)

        response = flask.make_response(body, int(code))
        response.mimetype = 'application/json'
        return response

    @classmethod
    def build_file_response(cls, body, code):
        #body = JsonSerializer.serialize(body)
        logger.info('CODE :: %s', code)
       
        response = flask.make_response(body, int(code))
        response.mimetype = 'application/vnd.ms-excel'
        return response