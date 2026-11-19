from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from redis import Redis, RedisError

import socket

BASE_DIR = Path(__file__).parent

hostname = socket.gethostname()

redis = Redis(host="redis", db=0)
app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

def getOptions():
    option_a = "hotdogs"
    option_b = "Lemonade"
    return option_a, option_b

def getNamespace():
    try:
        with open('/var/run/secrets/kubernetes.io/serviceaccount/namespace', 'r') as fp:
            return fp.read()
    except OSError:
        return "local"

@app.api_route("/", methods=["GET", "POST"], response_class=HTMLResponse)
def hello(request: Request, vote: Annotated[str | None, Form()] = None):
    option_a, option_b = getOptions()

    try:
        votesA = int(redis.get(option_a) or 0)
        votesB = int(redis.get(option_b) or 0)
    except RedisError:
        votesA = "cannot connect to Redis, counter disabled"
        votesB = "cannot connect to Redis, counter disabled"

    if request.method == 'POST':
        try:
            if vote == "a":
                votesA = redis.incr(option_a)
            else:
                votesB = redis.incr(option_b)
        except Exception as e:
            print(e)
            votesA = "An error occurred"
            votesB = "An error occurred"

    return templates.TemplateResponse(request, 'index.html', {
        'option_a': option_a,
        'option_b': option_b,
        'hostname': hostname,
        'namespace': getNamespace(),
        'votes_a': votesA,
        'votes_b': votesB,
    })
