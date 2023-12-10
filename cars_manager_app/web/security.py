import json
import os
from datetime import datetime, timedelta

from flask import request, jsonify, abort

from cars_manager_app.web.configuration import app
from cars_manager_app.email.configuration import MailConfig

def check_token(token) -> bool:
    fn = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tokens.json'))
    with open(fn, 'r') as file:
        data = json.load(file)
        tokens = data.get('tokens', [])
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        for t in tokens:
            if t['token'] == token and t['date'] >= current_time:
                return True
    return False


@app.route('/verify')
def verify_token():
    token = request.args.get('token')
    if not token:
        return jsonify({'error': 'No token in request'}), 400

    token_valid = check_token(token)
    if token_valid:
        return jsonify({'message': 'Token is valid'})

    return jsonify({'message': 'Token is invalid or expired'})

@app.route('/register', methods=['POST'])
def register_user():
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'No email in request'}), 400

    # Generating random token
    import secrets
    token = secrets.token_urlsafe(16)

    # Setting 1 month token expiration date
    expiration_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M')
    fn = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tokens.json'))

    # Adding token to json file
    with open(fn, 'r+') as file:
        data = json.load(file)
        tokens = data.get('tokens', [])
        tokens.append({'token': token, 'date': expiration_date})
        data['tokens'] = tokens
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()

    # Sending email with token
    MailConfig.send_register_token(sender_mail=email, recipient_email=email,token=token)
    return jsonify({"message": "Email with token sent."})

def token_required(route_function):
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            abort(401, description='Token is missing')
        elif not check_token(token):
            abort(401, description='Invalid or expired token')
        return route_function(*args, **kwargs)

    wrapper.__name__ = route_function.__name__
    return wrapper
