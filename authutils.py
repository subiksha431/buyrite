#!/usr/bin/env python

from enum import Enum
from functools import wraps

from flask import request

from buyrite.service.auth import AuthService
from buyrite.shared.error import ErrorApiModel
from buyrite.utils.logging import Logger
from buyrite.utils.restutils import ResponseBuilder, StatusCode

logger = Logger.build_logger()


class RoleCode(Enum):
    ADMIN = 'admin'
    CHARGEBACK_ADMIN = 'chargeback_admin'
    DEPT_MANAGER = 'dept_manager'
    BOT_USER = 'bot'

    @staticmethod
    def from_string(s: str):  # -> RoleCode:
        s = s.upper().strip()
        return RoleCode[s]


def extract_access_token(headers) -> str:
    key = 'Authorization'

    if key in headers:
        arr = headers[key].split()

        if len(arr) == 2 and arr[0].upper() == 'BEARER':
            return arr[1]

    return None


def _is_in_role(*args) -> StatusCode:
    # https://datatracker.ietf.org/doc/html/rfc6750#section-3.1
    access_token = extract_access_token(request.headers)

    if not access_token:
        return StatusCode.BAD_REQUEST

    service = AuthService()
    status_code, profile = service.get_profile(access_token)

    if not status_code.is_2xx_successful():
        return StatusCode.UNAUTHORIZED
    else:
        if len(args) == 0:
            return StatusCode.OK

        for role in args:
            if role == RoleCode.from_str(profile.role):
                return StatusCode.OK

        return StatusCode.FORBIDDEN


def _api_call_wrapper(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as ex:
            Logger.handle_exception(ex)
            return ResponseBuilder.build_error_response(StatusCode.SERVER_ERROR, ErrorApiModel(
                message='An error has occurred'
            ))

    return wrap


@_api_call_wrapper
def login_not_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        logger.info('Calling :: ' + f.__name__)
        return f(*args, **kwargs)
    return wrap


@_api_call_wrapper
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        logger.info('Calling :: ' + f.__name__)
        status_code = _is_in_role()

        if status_code.is_2xx_successful():
            return f(*args, **kwargs)
        else:
            return ResponseBuilder.build_error_response(status_code, ErrorApiModel(
                message='User must be logged in for this operation'
            ))

    return wrap


@_api_call_wrapper
def login_as_admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        logger.info('Calling :: ' + f.__name__)
        role: RoleCode = RoleCode.ADMIN
        status_code = _is_in_role(role)

        if status_code.is_2xx_successful():
            return f(*args, **kwargs)
        else:
            return ResponseBuilder.build_error_response(status_code, ErrorApiModel(
                message='User must be logged in as ' + role.name + ' for this operation'
            ))

    return wrap


@_api_call_wrapper    
def login_as_chargeback_admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        logger.info('Calling :: ' + f.__name__)
        role: RoleCode = RoleCode.CHARGEBACK_ADMIN
        status_code = _is_in_role(role)

        if status_code.is_2xx_successful():
            return f(*args, **kwargs)
        else:
            return ResponseBuilder.build_error_response(status_code, ErrorApiModel(
                message='User must be logged in as ' + role.name + ' for this operation'
            ))

    return wrap


@_api_call_wrapper    
def login_as_dept_manager_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        logger.info('Calling :: ' + f.__name__)
        role: RoleCode = RoleCode.DEPT_MANAGER
        status_code = _is_in_role(role)

        if status_code.is_2xx_successful():
            return f(*args, **kwargs)
        else:
            return ResponseBuilder.build_error_response(status_code, ErrorApiModel(
                message='User must be logged in as ' + role.name + ' for this operation'
            ))

    return wrap
