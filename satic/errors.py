class SaticError(Exception):
    kwargs = {}
    code = -9999
    msg = "Unknown error."

    @classmethod
    def get_msg(cls, **kwargs):
        return cls.msg



class InternalServerError(SaticError):
    code = -9998
    msg = "Internal Server occured: %(reason)s"

    @classmethod
    def get_msg(cls, **kwargs):
        return cls.msg % kwargs or {"reason": "Unknown Reason!"}
