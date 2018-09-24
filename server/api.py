from flask import Flask, request, Response, json, jsonify
from flask_cors import CORS
import session_manager

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello Fieldlab!"


@app.route('/init_disclosure', methods=['GET', 'POST'])
def init_disclosure_request():
    data = request.get_data()
    data_json = json.loads(data)
    attribute_request = data_json['attribute_request']
    description = data_json['description']

    session_id = session_manager.init_session(attribute_request, description)
    return json_response({'session_id': session_id})


@app.route('/get_session', methods=['GET', 'POST'])
def get_session():
    data = request.get_data()
    data_json = json.loads(data)
    session_id = data_json['session_id']

    response = session_manager.get_session(session_id)
    return json_response({'response': response})


@app.route('/deny_request', methods=['POST'])
def deny_request():
    data = request.get_data()
    data_json = json.loads(data)
    session_id = data_json['session_id']

    session_manager.end_session(session_id)
    return json_response({'response': "Session ended"})


@app.route('/get_active_sessions', methods=['GET'])
def get_active_sessions():
    return json_response(session_manager.active_sessions)


def json_response(data):
    response = Response(
        response=json.dumps(data),
        status=200,
        mimetype='application/json',
    )
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    app.run()
