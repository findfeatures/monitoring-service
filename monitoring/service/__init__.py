from monitoring.service.health_check import HealthCheckServiceMixin
from monitoring.service.service import MainServiceMixin


class MonitoringService(HealthCheckServiceMixin, MainServiceMixin):
    pass
