from satic.app import app
from satic.routes import route_list

for route in route_list:
    app.add_api_route(
        path=route["path"], endpoint=route["view"], methods=route["method"]
    )
