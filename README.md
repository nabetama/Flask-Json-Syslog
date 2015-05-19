# Flask-Json-Syslog
[![Downloads](https://pypip.in/download/Flask-Json-Syslog/badge.svg)](https://pypi.python.org/pypi/Flask-Json-Syslog/)
[![Supported Python versions](https://pypip.in/py_versions/Flask-Json-Syslog/badge.svg)](https://pypi.python.org/pypi/Flask-Json-Syslog/)
[![Latest Version](https://pypip.in/version/Flask-Json-Syslog/badge.svg?text=version)](https://pypi.python.org/pypi/Flask-Json-Syslog/)
[![License](https://pypip.in/license/Flask-Json-Syslog/badge.svg)](https://pypi.python.org/pypi/Flask-Json-Syslog/)

This is the Flask extension facility to output syslog of the Json form.

##  Installation

```sh
pip install flask-json-syslog
```

## Example

### config.py
```python

JSON_SYSLOG_LEVEL = 'info'# Log level
JSON_SYSLOG_NUMBER = 168  # syslog.LOG_LOCAL5
JSON_SYSLOG_FACILITY = 6  # syslog.LOG_INFO
```

### app.py
```python
from flask import g
from flask_json_syslog import FlaskJsonSyslog

app = Flask(__name__)
flask_json_syslog = FlaskJsonSyslog(app)

...

@app.before_request
def before_request():
    g.json_log = flask_json_syslog.put
```

### In your application
```python
g.json_log({'foo': 'bar'}, ...)
```

### (r)syslog.conf
```sh
...

$template json,"%msg%\n"
local5.* /var/log/local5.log;json

...
```

