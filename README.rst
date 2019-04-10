============================
 python-genieacs-nbi-client
============================

The package contains Rest API client implementation to communicate with [genieacs](https://github.com/genieacs/genieacs/) NBI.



Requirements
============

* Python 3.5 over


Setup
=====

::

  $ python -m pip install --user python-genieacs-nbi-client
  or
  (venv)$ python -m pip install python-genieacs-nbi-client

Usage
=====

::

  $ python
  >>> from python_genieacs_nbi_client import client
  >>> cl = client.Client("verbose": True, "address": "http://foo.bar")
  >>> nbi_resp_js = cl.dispatch_device_task(DEVICE_ID, {"name":"setParameterValues", "parameterValues":[["InternetGatewayDevice.ManagementServer.PeriodicInformEnable", 300, "xsd:int"]]})
  >>>

