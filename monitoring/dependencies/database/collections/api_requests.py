from monitoring.dependencies.database.collections import Collection
from monitoring.dependencies.database.models import ApiRequest


class ApiRequests(Collection):
    name = "api_requests"
    model = ApiRequest

    def create(self, user_id, token):
        # todo: fill this in!
        new_api_request = self.model()

        with self.db.get_session() as session:
            session.add(new_api_request)
