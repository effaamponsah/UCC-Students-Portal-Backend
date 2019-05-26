from flask import Flask, redirect, request, jsonify, url_for
import pymysql
from utils.user import User
import jwt
import datetime
import hashlib
def _login():
    if request.method == "GET":
        return jsonify(
            Success=False, Warning="GET method not allowed on this route. Use POST"
        )
    else:
        body = request.get_json()
        index = (body["indexnumber"]).upper()
        response = User(index, body["password"])
        if None in response:
            return jsonify(
                Success=False, Warning="Student not found. Enter correct Credentials"
            )
        else:
            auth_token = jwt.encode(
                {
                    "indexnumber": body["indexnumber"],
                    "id": response[0]['id'],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=5),
                },
                "226905605219861890656256635479281220067966797385942583903537",  # Use a more secured algorithm
                # i used a random to get 200 random integers
            )
            return jsonify(Success=True, Student=response[0], Token=auth_token.decode())
        # if body["indexnumber"] == "PS/CSC/15/0004" and body["password"] == "effa":
        #     # return jsonify({"Success": True})
        #     return redirect(url_for("index"))

        # else:
        #     return jsonify(Success=False, Warning=" Please provide correct credentials")
        # # return jsonify({"Success": True, "Message": "Welcome " + response["username"]})
