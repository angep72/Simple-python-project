from flask import Flask, request,jsonify

app = Flask(__name__)
@app.route("/get-users")
def home():
    user_Data={
        "users": [
            {"id":1, "name":"John Doe", "email":"john@example.com"},
            {"id":2, "name":"Jane Doe", "email":"jane@example.com"},
            {"id":3, "name":"Alice Johnson", "email":"alice@example.com"}
        ]
    }
    return jsonify(user_Data)




if __name__ == '__main__':
    app.run(debug=True)