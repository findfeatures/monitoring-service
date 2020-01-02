import walrus
from nameko import config
from nameko.extensions import Entrypoint


class NamekoRedisConsumerGroup(Entrypoint):
    def __init__(self, consumer_group, streams, **kwargs):
        self.consumer_group = consumer_group
        self.streams = streams
        self.redis_client = None

        super(NamekoRedisConsumerGroup, self).__init__(**kwargs)

    def setup(self):
        self.redis_client = walrus.Database().from_url(config.get("REDIS_URL"))
        self.consumer_group = self.redis_client.consumer_group(
            self.consumer_group, self.streams
        )

        self.consumer_group.create()

        # todo: investigate what this does!
        self.consumer_group.set_id(id="$")

    def start(self):
        self.container.spawn_managed_thread(
            self.run, identifier="NamekoRedisConsumerGroup.run"
        )

    def run(self):
        while True:
            # block pauses execution for number of milliseconds if no messages
            # are available
            message = self.consumer_group.read(count=1, block=1000)

            if message:
                # its quite deeply nested here...
                message = message[0][1][0]

                # decode messages from binary
                self.handle_message(
                    message[0].decode("utf8"),
                    dict(
                        (k.decode("utf8"), v.decode("utf8"))
                        for k, v in message[1].items()
                    ),
                )

    def handle_message(self, id, message):
        args = (id, message)
        kwargs = {}
        self.container.spawn_worker(self, args, kwargs)


consume = NamekoRedisConsumerGroup.decorator
