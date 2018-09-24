from flask import Flask, request, Response, json, jsonify, session, Session

app = Flask(__name__)
sess = Session()

@app.route('/')
def hello():
    return "Hello Fieldlab!"

@app.route('/init_disclosure', methods=['POST'])
def init_disclosure_request():
    data = request.get_data()

    session['key'] = 'value'
    return jsonify({"message": "OK"})

@app.route('/get')
def get_session():
    return session.get('key', 'not set')

def json_response(data):
    response = Response(
        response=json.dumps(data),
        status=200,
        mimetype='application/json',
    )
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
    sess.init_app(app)
    app.run()