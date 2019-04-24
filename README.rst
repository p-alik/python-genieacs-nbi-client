============================
 python-genieacs-nbi-client
============================

The package contains Rest API client implementation to communicate with `GenieACS NBI <https://github.com/genieacs/genieacs/>`_.

|travis-badge|_ |coveralls-badge|_

.. |travis-badge| image:: https://travis-ci.org/p-alik/python-genieacs-nbi-client.svg?branch=master
.. _travis-badge: https://travis-ci.org/p-alik/python-genieacs-nbi-client

.. |coveralls-badge| image:: https://coveralls.io/repos/github/p-alik/python-genieacs-nbi-client/badge.svg?branch=master
.. _coveralls-badge: https://coveralls.io/github/p-alik/python-genieacs-nbi-client?branch=master


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

