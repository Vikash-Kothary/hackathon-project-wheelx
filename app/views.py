#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
views.py -
"""
from flask import render_template
from app import app
from api import get_wheel_sets, get_trajectory_array, get_schedule


@app.route('/')
def home():
    return render_template('index.html', info=get_wheel_sets())


@app.route('/wheels')
def wheels():
    return render_template('wheels.html')


@app.route('/trajectory')
def trajectory():
    return render_template('trajectory.html', info=get_trajectory_array())


@app.route('/schedule')
def schedule():
    return render_template('schedule.html', info=get_schedule())
