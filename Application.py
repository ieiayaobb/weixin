__author__ = 'shenyineng'

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/validate', methods=['GET'])
def validate():
    signature = request.args.get('signature')
    echostr = request.args.get('echostr')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')

    print(signature)
    print(echostr)
    print(timestamp)
    print(nonce)

    return echostr


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)