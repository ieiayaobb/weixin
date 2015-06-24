__author__ = 'shenyineng'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/signature<signature>', methods=['GET'])
def signature(signature, echostr, timestamp, nonce):
    print(signature)
    print(echostr)
    print(timestamp)
    print(nonce)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)