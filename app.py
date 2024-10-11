from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.form['message']
    command = f'alexa_remote_control -e speak:"{message}"'
    os.system(command)
    return f'Message sent to Alexa: {message}'
@app.route('/volume', methods=['POST'])
def volume():
    vol = request.form['volume']
    command = f'alexa_remote_control -e vol:"{vol}"'
    os.system(command)
    return f'Volume increased: {vol}'
@app.route('/volume', methods=['GET'])
def volumeget():
    command = f'alexa_remote_control -z'
    os.system(command)
    result = os.popen(command).read()
    return f'Volume is:{result}'


if __name__ == '__main__':
    app.run(port=9900, host="0.0.0.0", debug=True)

