from satic.view.test import TestView
from satic.view.development.tracker import TrackerView

route_list = [
    {"path": "/test", "view": TestView, "method": ["GET", "POST"]},
    {"path": "/tracker", "view": TrackerView, "method": ["GET"]},
]
