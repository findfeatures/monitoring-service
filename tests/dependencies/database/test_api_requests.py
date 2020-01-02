import datetime

import pytest
from monitoring.dependencies.database.models import ApiRequest
from monitoring.dependencies.database.provider import Storage
from nameko.testing.services import dummy, entrypoint_hook


@pytest.fixture
def service_container(db, container_factory):
    class Service:
        name = "monitoring"

        storage = Storage()

        @dummy
        def append(self, *args, **kwargs):
            return self.storage.api_requests.append(*args, **kwargs)

    container = container_factory(Service)
    container.start()

    return container


def test_create_api_request(db, service_container):
    redis_message_id = "123-0"
    url = "test_url"
    method = "GET"
    duration = "1.231"
    status = "500 SOMETHING!"
    status_code = 500
    remote_addr = "localhost"

    with entrypoint_hook(service_container, "append") as append:
        append(
            redis_message_id, url, method, duration, status, status_code, remote_addr
        )

    assert db.session.query(ApiRequest).count() == 1

    result = (
        db.session.query(ApiRequest).filter_by(redis_message_id=redis_message_id).one()
    )

    assert result.url == url
    assert result.method == method
    assert result.duration == duration
    assert result.status == status
    assert result.status_code == status_code
    assert result.remote_addr == remote_addr
