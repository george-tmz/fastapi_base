# app/consumer.py

import aio_pika
import asyncio
from core.RabbitMQConnect import rabbitmq

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        print(f"Received message: {message.body.decode()}")

async def consume():
    await rabbitmq.connect()
    channel = rabbitmq.channel
    queue = await channel.declare_queue("my_queue", durable=True)
    await queue.consume(on_message)
    print("Waiting for messages...")
    await asyncio.Future()  # Run forever