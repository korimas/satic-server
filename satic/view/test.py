from satic.view.base import BaseView
from fastapi import Request


class TestView(BaseView):

    def get(self, request: Request):
        return "hello world"
