from monitoring.dependencies.database.provider import Storage, StorageWrapper
from monitoring.service import MonitoringService
from nameko.containers import ServiceContainer
from nameko.testing.services import replace_dependencies


def test_healthcheck(config, db, web_session):
    container = ServiceContainer(MonitoringService)
    replace_dependencies(container, storage=StorageWrapper(db, Storage.collections))
    container.start()

    response = web_session.get("/health-check")
    assert response.status_code == 200
