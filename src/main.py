import os

from flask import jsonify
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError


PUBLIC_KEY = os.environ.get("APPLICATION_PUBLIC_KEY")
verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))


def default_response():
    return jsonify(
        {
            "type": 4,
            "data": {
                "tts": False,
                "content": "Déjà vu!",
                "embeds": [],
                "allowed_mentions": {"parse": []},
            },
        }
    )


def verify_signature(request):
    """Validate request header against Discord application public key"""
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = request.data.decode("utf-8")

    try:
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
    except BadSignatureError:
        return ("invalid request signature", 401)


def main(request):
    """Main endpoint that responds to all HTTP requests.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    verify_signature(request)

    if request.json["type"] == 1:  # PING
        return jsonify({"type": 1})
    else:
        return default_response()
