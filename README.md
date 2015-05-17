# Flask-Json-Syslog

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

### rsyslog.conf
```sh
...

$template json,"%msg%\n"
local5.* /var/log/local5.log;json

...
```

