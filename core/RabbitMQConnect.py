from config.rabbitmp import RabbitMQ
import aio_pika


class RabbitMQConnect:
    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        if self.connection is None or self.connection.is_closed:
            self.connection = await aio_pika.connect_robust(
                host=RabbitMQ.RABBITMQ_HOST,
                port=RabbitMQ.RABBITMQ_PORT,
                login=RabbitMQ.RABBITMQ_USER,
                password=RabbitMQ.RABBITMQ_PASSWORD,
                virtualhost="bthost"
            )
            self.channel = await self.connection.channel()

    async def close(self):
        if self.connection and not self.connection.is_closed:
            await self.connection.close()

    async def publish(self, routing_key: str, message: str):
        await self.connect()
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()), routing_key=routing_key
        )


rabbitmq = RabbitMQConnect()
