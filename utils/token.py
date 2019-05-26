from flask import request, jsonify
import jwt
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "X-Access-Token" in request.headers:
            token = request.headers["X-Access-Token"]
        if not token:
            return jsonify(
                Success=False, Message="Access token is required to access resources"
            )

        try:
            data = jwt.decode(
                token, "226905605219861890656256635479281220067966797385942583903537"
            )
            indexnumber = (data["indexnumber"],)
            db_id = data["id"]
        except:
            return jsonify(Success=False, Message="Token is invalid or is expired")

        return f(indexnumber, db_id, *args, **kwargs)

    return decorated
