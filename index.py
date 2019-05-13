from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import jwt

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/")
def index():
    return jsonify({"Success": True, "Message": "UCC Students Portal"})


@app.route("/api/v1/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return jsonify(
            {"Success": False, "Warning": "GET method not allowed on this route. POST"}
        )
    else:
        response = request.get_json("username")
        return jsonify({"Success": True, "Message": "Welcome " + response["username"]})


if __name__ == "__main__":
    app.run(debug=True, port=1234)

