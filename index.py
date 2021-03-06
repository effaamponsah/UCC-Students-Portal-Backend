from flask import Flask, request, jsonify, make_response, redirect, url_for
from flask_cors import CORS
import jwt
import datetime

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
            return redirect(url_for("index"))

        else:
            return jsonify(
                {"Success": False, "Message": " Please provide correct credentials"}
            )
        # return jsonify({"Success": True, "Message": "Welcome " + response["username"]})


@app.route('/api/v1/info')
def info():
    return jsonify({"Success": True, "Message": "This is the route for the service information"})

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
        body = request.get_json()
        if not body:
            return jsonify(
                {"Success": False, "Message": "Please provide email as body"}
            )
        # check if email contains @ and . before you can send the email.
        # if possible use the students email
        if len(body["email"]) == 0:
            return jsonify(
                {
                    "Success": False,
                    "Message": "Please enter your email address. It cant be empty",
                }
            )
        else:
            # return jsonify({"Success": True, "Message": "Email sent"})
            return redirect(url_for("securityquestion"))
    return jsonify({"Success": True, "Message": ""})


@app.route("/api/v1/security")
def securityquestion():
    return jsonify({"Success": True, "Message": "Security question is on its way"})


@app.route("/test")
def test():

    token = jwt.encode(
        {
            "name": "Dennis",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
            "iss": "University of Cape Coast"
        },
        "Secret",
    )

    return jsonify({"Token": token.decode()}) 


@app.route("/api/v1/fees")
def fees():
    return jsonify({"Suucess": True, "Message": "This is fees route"})


@app.route("/api/v1/account/verify")
def verify():
    return jsonify({"Suucess": True, "Message": "This is verify route"})


@app.route("/api/v1/account/resetpassword")
def resetpassword():
    return jsonify({"Suucess": True, "Message": "This is reset route"})


@app.route("/api/v1/timetable")
def timetable():
    return jsonify(
        {"Success": True, "Message": "The timetable will be displayed in this route"}
    )


@app.route('/api/v1/register')
def registration():
    return jsonify({"Success": True, "Message": "Courses for the semester open for registration will be here"})

@app.route("/api/v1/account/logout")
def logout():
    return jsonify({"Success": True, "Message": "Logout successfull"})


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="192.168.42.163")

