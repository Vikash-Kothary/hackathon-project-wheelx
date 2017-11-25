#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
views.py -
"""
from flask import render_template
from app import app
from api import get_trajectory_array


@app.route('/parts')
def view_all_parts():
    return render_template('trajectory.html', info=get_trajectory_array())
