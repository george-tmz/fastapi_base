from fastapi import FastAPI
import httpx

app = FastAPI()

def sendVideo():
    url = ""
    response = httpx.get(url)
    return response.json()