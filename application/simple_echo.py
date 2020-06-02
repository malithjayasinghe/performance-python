from flask import request
from flask import Flask


simple_echo_app = Flask(__name__)

@simple_echo_app.route('/uploader', methods=['POST'])
def read_data():
    return str(request.json)

