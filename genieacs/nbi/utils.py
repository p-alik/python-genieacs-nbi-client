"""genieacs.nbi.utils."""
import json
import urllib.request


def build_request(url, method="GET", data=None):
    """Prepare and return urllib.request.Request."""
    js_str = json.dumps(data).encode("utf-8") if data is not None else None
    return urllib.request.Request(
        url,
        method=method,
        data=js_str
    )


def build_post_request(url, data):
    """Prepare and return urllib.request.Request(method=POST,...)."""
    return build_request(url, method="POST", data=data)
