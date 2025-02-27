from config.rabbitmp import RabbitMQ
import aio_pika


class RabbitMQConnect:
    def __init__(self, url: str):
        self.url = url
        self.connection = None
        self.channel = None

    async def connect(self):
        if self.connection is None or self.connection.is_closed:
            self.connection = await aio_pika.connect_robust(self.url)
            self.channel = await self.connection.channel()

    async def close(self):
        if self.connection and not self.connection.is_closed:
            await self.connection.close()

    async def publish(self, routing_key: str, message: str):
        await self.connect()
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()), routing_key=routing_key
        )


rabbitmq = RabbitMQConnect(
    url=f"amqp://{RabbitMQ.RABBITMQ_USER}:{RabbitMQ.RABBITMQ_PASSWORD}@{RabbitMQ.RABBITMQ_HOST}:{RabbitMQ.RABBITMQ_PORT}"
)
