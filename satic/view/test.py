from satic.view.base import BaseView
from fastapi import Request
import logging

LOG = logging.getLogger(__name__)

class TestView(BaseView):

    def get(self, request: Request):
        LOG.debug("TestView get method called")
        return ["hello world"], 100
