from satic.view.test import TestView

route_list = [
    {
        "path": "/test",
        "view": TestView,
        "method": ["GET", "POST"]
    }
]