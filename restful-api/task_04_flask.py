from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({'error': 'User not found'}), 404


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    elif "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    elif data['username'] in users:
        return jsonify({"error": "Username already exists"}), 409
    else:
        users[data['username']] = data
        return jsonify({
            "message": "User added",
            "user": data
        }), 201


if __name__ == "__main__":
    app.run()