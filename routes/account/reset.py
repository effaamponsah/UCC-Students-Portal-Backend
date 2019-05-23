from flask import Flask, redirect, request, jsonify, url_for
import pymysql


def _reset():
    if request.method != "POST":
        return jsonify(
            Success=False,
            Message=request.method + " is not supported. Use POST instead",
        )
    else:
        body = request.get_json()
        if not body:
            return jsonify(Success=False, Message="Please provide email as body")
        # check if email contains @ and . before you can send the email.
        # if possible use the students email
        if len(body["email"]) == 0:
            return jsonify(
                Success=False,
                Message="Please enter your email address. It cant be empty",
            )
        else:
            # write a function to send emails using smtplib
            return jsonify(Success=True, Message="Email sent")
    # return jsonify({"Success": True, "Message": ""})
