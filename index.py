from flask import Flask, request, jsonify, make_response, redirect, url_for
from flask_cors import CORS
import jwt

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/")
def index():
    return jsonify({"Success": True, "Message": "Welcome UCC Students Portal"})


@app.route("/api/v1/login", methods=["POST", "GET"])
# Try and add regular expressions on the index numbers
def login():
    if request.method == "GET":
        return jsonify(
            {"Success": False, "Warning": "GET method not allowed on this route. POST"}
        )
    else:
        body = request.get_json()
        if body["indexnumber"] == "PS/CSC/15/0004" and body["password"] == "effa":
            # return jsonify({"Success": True})
            return redirect(url_for('index'))

        else:
            return jsonify(
                {"Success": False, "Message": " Please provide correct credentials"}
            )
        # return jsonify({"Success": True, "Message": "Welcome " + response["username"]})


@app.route("/api/v1/reset", methods=["POST", "GET"])
def reset():
    if request.method != "POST":
        return jsonify(
            {
                "Success": False,
                "Message": request.method + " is not supported. Use POST instead",
            }
        )
    else:
        email = request.get_json("email")

        # check if email contains @ and . before you can send the email.
        # if possible use the students email
        if len(email) == 0:
            return jsonify(
                {"Success": False, "Message": "Please enter your email address"}
            )
        else:
            return jsonify({"Success": True, "Message": "Email sent"})
    return jsonify({"Success": True, "Message": ""})


@app.route("/api/v1/logout")
def logout():
    return jsonify({"Success": True, "Message": "Logout successfull"})


# @app.route("/test")
# def test():
#     import datetime

#     token = jwt.JWT.encode(
#         {
#             "name": "Dennis",
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
#         },
#         "Secret",
#     )

#     return jsonify({"Token": token.decode("UTF-C")})


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="192.168.42.163")

