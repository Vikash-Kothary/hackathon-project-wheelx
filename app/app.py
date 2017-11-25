#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
app.py - 
"""

from flask import Flask

app = Flask(__name__)
app.debug = True

DATABASE = {
    'system': 'postgresql',
    'user': 'postgres',
    'password': 'password',
    'db_name': 'wheels',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# '{0}://{1}:{2}@{3}:{4}/{5}.db'.format(
# DATABASE['system'], DATABASE['user'], DATABASE['password'],
# DATABASE['host'], DATABASE['port'], DATABASE['db_name'])


@app.route('/')
def success():
    return 'Python is working'

if __name__ == '__main__':
    app.run()
