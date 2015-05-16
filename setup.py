#coding: utf-8

"""
Flask-Json-SysLog
-----------------

"""
from setuptools import setup


setup(
    name='Flask-Json-Syslog',
    version='0.1',
    url='http://github.com/nabetama/flask-json-syslog/',
    license='BSD',
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
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
