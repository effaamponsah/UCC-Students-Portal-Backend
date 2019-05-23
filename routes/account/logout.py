
from flask import Flask, request, jsonify

def _logout():
    if request.method != "POST":
        return jsonify(Success=False, Message="Please use post")
    return jsonify(Success = True, Message ="Logout successfull")