from flask import Flask, jsonify

def render_FAQ():
    return jsonify(Success=True, Message= "This is FAQ")