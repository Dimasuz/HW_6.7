# from flask import jsonify


class ApiError(Exception):
    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message


# def error_handler(error: ApiError):
#    response = jsonify({"status": "error", "description": error.message})
#    response.status_code = error.status_code
#    return response