import pytest
from mock import ANY, call
from monitoring.exceptions.monitoring import UnrecognizedMonitorName
from monitoring.service import MonitoringService
from nameko.testing.services import entrypoint_hook, replace_dependencies
from nameko.testing.utils import get_container


def test_create_user_successful(config, db, runner_factory):
    runner = runner_factory(MonitoringService)
    container = get_container(runner, MonitoringService)
    storage = replace_dependencies(container, "storage")
    runner.start()

    storage.api_requests.append.return_value = None

    with entrypoint_hook(
        container, "consume_monitoring_stream"
    ) as consume_monitoring_stream:
        consume_monitoring_stream(
            "123",
            {
                "__MONITOR_NAME": "API_REQUEST",
                "url": "url",
                "method": "method",
                "duration": "duration",
                "status": "status",
                "status_code": 1,
                "remote_addr": "remote_addr",
            },
        )

    assert storage.api_requests.append.call_args == call(
        "123", "url", "method", "duration", "status", 1, "remote_addr"
    )


def test_raises_if_message_unrecognised(config, db, runner_factory):
    runner = runner_factory(MonitoringService)
    container = get_container(runner, MonitoringService)
    runner.start()

    with entrypoint_hook(
        container, "consume_monitoring_stream"
    ) as consume_monitoring_stream:
        with pytest.raises(UnrecognizedMonitorName):
            consume_monitoring_stream("123", {"__MONITOR_NAME": "DONT KNOW MESSAGE"})
