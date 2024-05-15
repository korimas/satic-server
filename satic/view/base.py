from fastapi import Request, Depends
from fastapi.responses import JSONResponse
from satic.errors import SaticError, InternalServerError
from typing import Any


class BaseView(object):
    """Each URL shares a single view object for all requests."""

    depends = None
    __name__ = None

    def __call__(self, request: Request):
        method = request.method.lower()

        if hasattr(self, method):
            handler = getattr(self, method)
        else:
            return JSONResponse(
                status_code=405,
                content=self.gen_response(False, -1, "Method Not Allowed!"),
            )

        try:
            result = handler(request)
            return JSONResponse(
                status_code=200,
                content=self.gen_response(
                    True,
                    result,
                ),
            )
        except SaticError as e:
            return JSONResponse(
                status_code=500,
                content=self.gen_response(False, None, e.code, e.get_msg()),
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content=self.gen_response(
                    False,
                    None,
                    InternalServerError.code,
                    InternalServerError.get_msg(reason=str(e)),
                ),
            )

    @classmethod
    def gen_response(
        cls, success: bool, result: Any, error_code: int = 0, error_msg: str = None
    ):
        response = {"success": success}
        if success:
            response["result"] = result
        else:
            response["error"] = {"code": error_code, "msg": error_msg}
        return response
