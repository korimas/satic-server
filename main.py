from satic.app import app
from satic.routes import route_list
from satic.log import init_log
import logging

LOG = logging.getLogger(__name__)

init_log()
LOG.debug("start satic app")
for route in route_list:
    app.add_api_route(
        path=route["path"], endpoint=route["view"](), methods=route["method"]
    )
LOG.debug("add route success")