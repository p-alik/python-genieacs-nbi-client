"""genieacs.nbi.utils."""
from __future__ import absolute_import
import json
import urllib2


def build_request(url, method="GET", data=None):
    """Prepare and return urllib.request.Request."""
    js_str = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib2.Request(
        url,
        data=js_str
    )
    req.get_method = lambda: method

    return req


def build_post_request(url, data):
    """Prepare and return urllib.request.Request(method=POST,...)."""
    return build_request(url, method="POST", data=data)
