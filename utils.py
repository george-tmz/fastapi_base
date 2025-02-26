import socket
import uuid


def get_current_ip():
    hostname = socket.gethostname()  # 获取主机名
    ip_address = socket.gethostbyname(hostname)  # 根据主机名获取 IP 地址
    return ip_address


def get_uuid():
    return str(uuid.uuid4())
