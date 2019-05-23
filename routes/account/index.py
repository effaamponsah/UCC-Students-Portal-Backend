from flask import Flask, jsonify

def account():
    return jsonify(Success= True, Message="Account route")