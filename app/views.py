#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
views.py -
"""
from flask import render_template
from app import app
from api import get_trajectory_array


@app.route('/')
def view_all_parts():
    return render_template('index.html', info=flagged_wheels())

@app.route('/wheels')
def view_all_parts():
    return render_template('wheels.html')    

@app.route('/trajectory')
def view_all_parts():
    return render_template('trajectory.html', info=get_trajectory_array())

@app.route('/schedule')
def view_all_parts():
    return render_template('schedule.html', info=get_all_flagged_data())    
