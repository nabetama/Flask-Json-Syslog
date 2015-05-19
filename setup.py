from setuptools import setup


with open("README.rst",  "rt") as f: readme = f.read()


setup(
    name='Flask-Json-Syslog',
    version='0.1.28',
    url='https://github.com/nabetama/Flask-Json-Syslog',
    license='MIT',
    author='Mao Nabeta',
    author_email='mao.nabeta@gmail.com',
    description='Output syslog of the json format.',
    long_description=readme,
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
