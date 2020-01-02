import datetime
import logging

import monitoring.entrypoint as redis_stream
from monitoring.exceptions.monitoring import UnrecognizedMonitorName
from monitoring.service.base import ServiceMixin


logger = logging.getLogger(__name__)


class MainServiceMixin(ServiceMixin):
    @redis_stream.consume("cg-monitoring-service", ["MONITORING_STREAM"])
    def consume_monitoring_stream(self, message_id, message):

        monitor_name = message["__MONITOR_NAME"]

        logger.info(
            f"{datetime.datetime.utcnow().isoformat()}: consuming {monitor_name} with id {message_id}"
        )

        if monitor_name == "API_REQUEST":
            self.storage.api_requests.append(
                message_id,
                message.get("url"),
                message.get("method"),
                message.get("duration"),
                message.get("status"),
                message.get("status_code"),
                message.get("remote_addr"),
            )
        else:
            raise UnrecognizedMonitorName(f"{monitor_name} is not recognized")
