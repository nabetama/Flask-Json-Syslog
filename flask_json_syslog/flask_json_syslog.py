# -*- coding: utf-8 -*-

import syslog


json_available = True
json = None
try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        json_available = False


def jsonify(dict_data, *args, **kwargs):
    if not json_available:
        raise RuntimeError('simplejson not installed')
    return json.dumps(dict(dict_data, *args, **kwargs), indent=None)


class JsonSysLog(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('JSON_SYSLOG_LEVEL', 'info')
        app.config.setdefault('JSON_SYSLOG_NUMBER',  syslog.LOG_LOCAL5)
        app.config.setdefault('JSON_SYSLOG_FACILITY',  syslog.LOG_INFO)
        self.log_level = app.config['JSON_SYSLOG_LEVEL']
        self.log_number = app.config['JSON_SYSLOG_NUMBER']
        self.facility  = app.config['JSON_SYSLOG_FACILITY']

    def put(self, dict_data, **kwargs):
        assert isinstance(dict_data, dict), "dict_data is must be dict!"
        self.dict_data = dict_data.copy()
        self.dict_data.update(kwargs)
        self.syslog_output()

    def syslog_output(self):
        syslog.openlog(self.log_level, syslog.LOG_PID, self.log_number)
        syslog.syslog(self.facility, jsonify(self.dict_data))

