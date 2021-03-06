from http import HTTPStatus

from main.extensions.api_codes import APICode
from main.extensions.exceptions import APIException


class LogicalValidationException(APIException):
    code = APICode.LOGICAL_VALIDATOR_ERROR
    http_status = HTTPStatus.BAD_REQUEST

    def __init__(self, message=APICode.LOGICAL_VALIDATOR_ERROR.description,
                 extra=None):
        super().__init__(
            code=APICode.LOGICAL_VALIDATOR_ERROR,
            http_status=HTTPStatus.BAD_REQUEST,
            message=message,
            extra=extra
        )

    def __str__(self):
        return "logical validation errors"
