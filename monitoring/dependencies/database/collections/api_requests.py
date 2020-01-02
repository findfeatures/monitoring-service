from monitoring.dependencies.database.collections import Collection
from monitoring.dependencies.database.models import ApiRequest


class ApiRequests(Collection):
    name = "api_requests"
    model = ApiRequest

    def append(
        self, redis_message_id, url, method, duration, status, status_code, remote_addr
    ):
        # todo: fill this in!
        new_api_request = self.model(
            redis_message_id=redis_message_id,
            url=url,
            method=method,
            duration=duration,
            status=status,
            status_code=status_code,
            remote_addr=remote_addr,
        )

        with self.db.get_session() as session:
            session.add(new_api_request)
