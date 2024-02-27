from functools import wraps

import jwt
from flask import request, make_response, current_app, jsonify, g


def valid_token(func):
    """
    checks if the authorization token is valid
    :param func: callback function
    :return:
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        return make_response('token is invalid or missing!', 401)

    return decorator


def customer_required(func):
    """
    checks if the userrole is 'customer' or higher
    :param func: callback function
    :return:
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        return make_response('You shall not pass!', 401)
    return decorator


def employee_required(func):
    """
    checks if the userrole is 'employee' or higher
    :param func: callback function
    :return:
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        return make_response('You shall not pass!', 401)
    return decorator


def admin_required(func):
    """
    checks if the userrole is 'admin'
    :param func: callback function
    :return:
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        return make_response('You shall not pass!', 401)
    return decorator
