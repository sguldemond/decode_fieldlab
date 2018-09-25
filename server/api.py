from flask import Flask, request, Response, json, session, send_from_directory
from flask_cors import CORS
import session_manager
import data_source
import validator

app = Flask(__name__, static_url_path='/../../dist')
CORS(app)

# data_source.generate_dummy_data()
#
# @app.route('/decode/<path:path>')
# def send_web(path):
#     return send_from_directory('', path)


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

    attribute_request = session_manager.get_session(session_id)['request']
    validator_response = validator.check(attribute_request, brp_data)

    active_session = session_manager.append_session_data(session_id, {'request_valid': validator_response})

    # can not be ended here, since requestor needs to access data still
    # session_manager.end_session(session_id)

    return json_response(active_session)


@app.route('/deny_request', methods=['POST'])
def deny_request():
    data = request.get_data()
    data_json = json.loads(data)
    session_id = data_json['session_id']

    response = session_manager.end_session(session_id)

    return json_response({'response': response})


@app.route('/get_active_sessions', methods=['GET'])
def get_active_sessions():
    return json_response(session_manager.active_sessions)


@app.route('/login', methods=['POST'])
def login():
    session['logged_in'] = True


# @app.route('/logout')
# def login():
#     session['logged_in'] = False


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
