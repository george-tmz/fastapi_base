import aio_pika
import asyncio

from config.rabbitmp import RabbitMQ


async def main():
    # 连接到 RabbitMQ
    connection = await aio_pika.connect_robust(
        host="115.159.205.90",
        port=5672,
        login="admin",
        password="oI66U7NszO8MyP1X",
        virtualhost="bthost"
    )

    # 执行其他操作，例如创建通道等
    async with connection:
        channel = await connection.channel()
        # 继续进行消息处理等
        print("Connected to RabbitMQ")


# 运行主程序
asyncio.run(main())