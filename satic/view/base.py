from fastapi import Request, Depends
from fastapi.responses import JSONResponse
from satic.errors import SaticError, InternalServerError
from typing import Any
import logging

LOG = logging.getLogger(__name__)

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
                content=self.gen_response(
                    success=False, error_code=-1, error_msg="Method Not Allowed!"
                ),
            )

        try:
            total = -1
            result = handler(request)
            if isinstance(result, tuple) and len(result) == 2:
                total = result[1]
                result = result[0]

            return JSONResponse(
                status_code=200,
                content=self.gen_response(
                    success=True,
                    result=result,
                    total=total,
                ),
            )
        except SaticError as e:
            LOG.exception("Failed to handle request.")
            return JSONResponse(
                status_code=500,
                content=self.gen_response(
                    success=False, error_code=e.code, error_mgs=e.get_msg()
                ),
            )
        except Exception as e:
                LOG.exception("Failed to handle request.")
                return JSONResponse(
                status_code=500,
                content=self.gen_response(
                    success=False,
                    error_code=InternalServerError.code,
                    error_msg=InternalServerError.get_msg(reason=str(e)),
                ),
            )

    @classmethod
    def gen_response(
        cls,
        success: bool,
        result: Any = None,
        total: int = 0,
        error_code: int = 0,
        error_msg: str = None,
    ):
        response = {"success": success}
        if success:
            response["result"] = result or {}
        else:
            response["error"] = {"code": error_code, "msg": error_msg}

        if total >= 0:
            response["total"] = total

        return response
