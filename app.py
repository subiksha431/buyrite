#!/usr/bin/env python

from flask import Flask

from buyrite.api import login
from buyrite.api import logout
from buyrite.api import buyriteusers

from buyrite.api import store
from buyrite.api import vendor
from buyrite.api import product



app = Flask(__name__)

app.register_blueprint(store.blueprint)
app.register_blueprint(vendor.blueprint)
app.register_blueprint(product.blueprint)
app.register_blueprint(login.blueprint)
app.register_blueprint(logout.blueprint)
app.register_blueprint(buyriteusers.blueprint)


@app.after_request
def after_request(response):
    headers = response.headers
    headers['Access-Control-Allow-*'] = '*'
    headers['Access-Control-Allow-Credentials'] = True
    headers['Access-Control-Allow-Headers'] = '*'
    headers['Access-Control-Expose-Headers'] = '*'
    headers['Access-Control-Allow-Methods'] = '*'
    headers['Access-Control-Allow-Origin'] = '*'
    headers['node-cache'] = 'Missed node-cache'
    return response


if __name__ == '__main__':
    app.run()
