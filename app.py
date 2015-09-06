#-*-coding:utf-8-*-

from flask import Flask, request, jsonify
from config import APP_ID, APP_SECRET, CORS_ALLOW_ORIGIN
from cache import cache
from sign import Signer


app = Flask(__name__)
cache.init_app(app)

signer = Signer(APP_ID, APP_SECRET)


@app.route('/api')
def api():
    url = request.args['url']
    ret = signer.sign(url)
    resp = jsonify(ret)
    resp.headers['Access-Control-Allow-Origin'] = CORS_ALLOW_ORIGIN
    return resp


if __name__ == '__main__':
    app.run(debug=True)