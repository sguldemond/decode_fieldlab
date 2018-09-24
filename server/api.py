from flask import Flask, request, Response, json, jsonify
from flask_cors import CORS
import session_manager
import data_source

app = Flask(__name__)
CORS(app)

data_source.generate_dummy_data()


@app.route('/')
def hello():
    return "Hello Fieldlab!"


@app.route('/init_disclosure', methods=['POST'])
def init_disclosure_request():
    data = request.get_data()
    data_json = json.loads(data)
    attribute_request = data_json['attribute_request']
    description = data_json['description']

    session_id = session_manager.init_session(attribute_request, description)
    return json_response({'session_id': session_id})


@app.route('/get_session', methods=['POST'])
def get_session():
    data = request.get_data()
    data_json = json.loads(data)
    session_id = data_json['session_id']

    response = session_manager.get_session(session_id)
    return json_response({'response': response})


@app.route('/get_session_status', methods=['POST'])
def get_session_status():
    data = request.get_data()
    data_json = json.loads(data)
    session_id = data_json['session_id']

    response = session_manager.get_session_status(session_id)
    return json_response({'response': response})


@app.route('/accept_request', methods=['POST'])
def accept_request():
    data = request.get_data()
    data_json = json.loads(data)
    session_id = data_json['session_id']
    username = data_json['username']

    brp_data = data_source.get_data(username)
    active_session = session_manager.append_session_data(session_id, brp_data)

    # session_manager.end_session(session_id)

    return json_response(active_session)


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
    app.run(host='0.0.0.0')
