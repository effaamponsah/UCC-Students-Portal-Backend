from flask import Flask, redirect, request, jsonify, url_for
import pymysql

def _login():
    if request.method == "GET":
        return jsonify(
            Success=False, Warning="GET method not allowed on this route. Use POST"
        )
    else:
        body = request.get_json()
        if body["indexnumber"] == "PS/CSC/15/0004" and body["password"] == "effa":
            # return jsonify({"Success": True})
            return redirect(url_for("index"))

        else:
            return jsonify(Success=False, Warning=" Please provide correct credentials")
        # return jsonify({"Success": True, "Message": "Welcome " + response["username"]})
