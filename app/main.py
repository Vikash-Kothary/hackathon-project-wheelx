#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
main.py - 
"""

from __init__ import *

from app import app
from models import db
#from auth import *
#from admin import admin
from api import *
from views import *

db.init_app(app)
# db.create_all()


def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
