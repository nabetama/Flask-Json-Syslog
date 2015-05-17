"""
Flask-Json-Syslog
=================

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
~~~~~~~~~~~~

.. code:: sh

    ...

    $template json,\"%msg%\\n\"
    local5.* /var/log/local5.log;json

    ...

Links
`````

* `website <https://github.com/nabetama/Flask-Json-Syslog>`_
"""
from setuptools import setup


setup(
    name='Flask-Json-Syslog',
    version='0.1.24',
    url='https://github.com/nabetama/Flask-Json-Syslog',
    license='MIT',
    author='Mao Nabeta',
    author_email='mao.nabeta@gmail.com',
    description='Output syslog of the json format.',
    long_description=__doc__,
    packages=['flask_json_syslog'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    provides=['Flask', 'syslog', 'json'],
    keywords=['Flask', 'syslog', 'json'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
