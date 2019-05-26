from flask import Flask, redirect, request, jsonify, url_for

# import pymysql
# from utils.user import ChangePassword
from utils.user import ChangePassword
from utils.token import token_required


@token_required
def _changepassword(indexnumber, db_id):
    if request.method != "PUT":
        return jsonify(
            Success=False,
            Message=request.method + " is not supported. Use POST instead",
        )
    else:
        # body = request.get_json()
        # if not body:
        #     return jsonify(Success=False, Message="Please provide password as body")
        # if body["password"] != body["newpassword"]:
        #     jsonify(Success=False, Message="Passwords are not the same")
        # else:
        #     # Make an update to the database for the password field
        #     # Check whether the person is actually a user.
        #     jsonify(Success=True, Message="Password successfuly changed")
        #     # Send an email to the user that his password has been updated
        body = request.get_json()
        if not body:
            return jsonify(Success=False, Message="Please provide passwords")
        else:
            # ResetPassword(body["oldpassword"], body["newpassword"])
            changed_handler = ChangePassword(
                indexnumber[0], body["oldpassword"], body["newpassword"]
            )
            if changed_handler == True:
                return jsonify(
                    Success=changed_handler, Message="Password successfully changed"
                )
            else:
                return jsonify(
                    Success=changed_handler,
                    Message="Please Confirm that your old password is correct",
                )

