Flask-Json-Syslog
=================

|Downloads| |Supported Python versions| |Latest Version| |License|

This is the Flask extension facility to output syslog of the Json form.

Installation
------------

.. code:: sh

    pip install flask-json-syslog

Example
-------

config.py
~~~~~~~~~

.. code:: python


    JSON_SYSLOG_LEVEL = 'info'# Log level
    JSON_SYSLOG_NUMBER = 168  # syslog.LOG_LOCAL5
    JSON_SYSLOG_FACILITY = 6  # syslog.LOG_INFO

app.py
~~~~~~

.. code:: python

    from flask import g
    from flask_json_syslog import FlaskJsonSyslog

    app = Flask(__name__)
    flask_json_syslog = FlaskJsonSyslog(app)

    ...

    @app.before_request
    def before_request():
        g.json_log = flask_json_syslog.put

In your application
~~~~~~~~~~~~~~~~~~~

.. code:: python

    g.json_log({'foo': 'bar'}, ...)

(r)syslog.conf
~~~~~~~~~~~~~~

.. code:: sh

    ...

    $template json,"%msg%\n"
    local5.* /var/log/local5.log;json

    ...

.. |Downloads| image:: https://pypip.in/download/Flask-Json-Syslog/badge.svg
   :target: https://pypi.python.org/pypi/Flask-Json-Syslog/
.. |Supported Python versions| image:: https://pypip.in/py_versions/Flask-Json-Syslog/badge.svg
   :target: https://pypi.python.org/pypi/Flask-Json-Syslog/
.. |Latest Version| image:: https://pypip.in/version/Flask-Json-Syslog/badge.svg?text=version
   :target: https://pypi.python.org/pypi/Flask-Json-Syslog/
.. |License| image:: https://pypip.in/license/Flask-Json-Syslog/badge.svg
   :target: https://pypi.python.org/pypi/Flask-Json-Syslog/
