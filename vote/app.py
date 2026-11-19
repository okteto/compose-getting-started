from flask import Flask, render_template, request, make_response
from redis import Redis, RedisError

import socket

hostname = socket.gethostname()

redis = Redis(host="redis", db=0)
app = Flask(__name__)

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

@app.route("/", methods=['POST','GET'])
def hello():
    option_a, option_b = getOptions()

    try:
        votesA = int(redis.get(option_a) or 0)
        votesB = int(redis.get(option_b) or 0)
    except RedisError:
        votesA = "cannot connect to Redis, counter disabled"
        votesB = "cannot connect to Redis, counter disabled"

    if request.method == 'POST':
        try:
            vote = request.form['vote']
            if vote == "a":
                votesA = redis.incr(option_a)
            else:
                votesB = redis.incr(option_b)
        except Exception as e:
            print(e)
            votesA = "An error occurred"
            votesB = "An error occurred"

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
        namespace=getNamespace(),
        votes_a=votesA,
        votes_b=votesB,
    ))
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
