import logging

import monitoring.entrypoint as redis_stream
from monitoring.service.base import ServiceMixin


logger = logging.getLogger(__name__)


class MainServiceMixin(ServiceMixin):
    @redis_stream.consume("cg-monitoring-service", ["MONITORING_STREAM"])
    def consume_monitoring_stream(self, message_id, message):
        self.storage.api_requests.append(
            message_id,
            message.get("url"),
            message.get("method"),
            message.get("duration"),
            message.get("status"),
            message.get("status_code"),
            message.get("remote_addr"),
        )
