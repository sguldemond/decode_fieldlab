from uuid import uuid4

active_sessions = []


def init_session(attribute_request, description):
    new_session_id = str(uuid4())
    new_session = {'request': attribute_request,
                   'description': description,
                   'id': new_session_id}
    active_sessions.append(new_session)
    return new_session_id


def get_session(session_id):
    print(active_sessions)
    for session in active_sessions:
        if session['id'] == session_id:
            return session

    return "No session found"


def end_session(session_id):
    for session in active_sessions:
        if session['id'] == session_id:
            session_to_end = session

    active_sessions.remove(session_to_end)
    print("Session ended with ID: " + session_to_end)


