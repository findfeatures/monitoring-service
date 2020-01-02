from monitoring.dependencies.database.provider import Storage


class ServiceMixin:
    name = "monitoring"

    storage = Storage()
