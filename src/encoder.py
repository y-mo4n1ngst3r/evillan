import base64
import urllib.parse
import html
import random

ENCODING_METHODS = {
    "base64": lambda payload: base64.b64encode(payload.encode()).decode(),
    "url": lambda payload: urllib.parse.quote(payload),
    "html": lambda payload: html.escape(payload),
    "reverse": lambda payload: payload[::-1],
    "rot13": lambda payload: codecs.encode(payload, "rot_13"),
}

def encode_payload(payload, methods, depth):
    """Apply encoding methods to a payload."""
    for _ in range(depth):
        method = random.choice(methods)
        payload = ENCODING_METHODS[method](payload)
    return payload

def encode_payloads(input_file, methods, depth, extra_payloads=None):
    """Read payloads from a file, encode them, and return only the payloads."""
    with open(input_file, "r") as file:
        payloads = [line.strip() for line in file]
    if extra_payloads:
        payloads.extend(extra_payloads)

    # Encode payloads and return only the payloads (no methods)
    return [encode_payload(payload, methods, depth) for payload in payloads]
