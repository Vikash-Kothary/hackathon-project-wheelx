#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
api.py -
"""

# Table: Inspection
# PartId, MeasureDateDate, PanSize, MayCutSize, DaysSinceCut, CutStatus

# Table: Parts
# PartId, Unit, Vehicale, SerialNo, Description, Position


# Query Inspections by Part
# Query Parts by Vechical.

from flask import jsonify, request, abort
from app import app
from models import load_data

wheel_sets = [
    {
        'train_unit': 220001,
        'vehicle_in_unit': 60301,
        'serial_no': u'M66000325RG',
        'axle_poition': 2
    },
    {
        'train_unit': 220001,
        'vehicle_in_unit': 60301,
        'serial_no': u'M66000325RG',
        'axle_poition': 3
    }
]

slots_available = [
    {
        'datetime': 20171125,
        'unit_code': 1,
        'vehicle_id': 1,
        'axis_positions': 2
    },
    {
        'datetime': 20171126,
        'unit_code': 1,
        'vehicle_id': 1,
        'axis_positions': 2
    }
]


@app.route('/wheel_sets', methods=['GET'])
def view_all_wheel_sets():
    return jsonify({'wheel_sets': wheel_sets})
# return render_template('view_all.html', parts=parts.query.all())


@app.route('/slots_available', methods=['GET'])
def view_all_slots_available():
    return jsonify({'slots_available': slots_available})


@app.route('/add_wheel_sets', methods=['POST'])
def add_wheel_sets():
    if not request.json or not 'title' in request.json:
        abort(400)
    # task = {
    #     'id': tasks[-1]['id'] + 1,
    #     'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }
    # tasks.append(task)
    # return jsonify({'task': task}), 201


@app.route('/delete_wheel_set/<int:train_id>', methods=['DELETE'])
def delete_task(train_id):
    # task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    # tasks.remove(task[0])
    # return jsonify({'result': True})


# @app.route('/flagged_wheels', methods=['GET']):
# def get_all_flagged_wheels():
#     # TODO: Natural join schedule and wheels
#     return jsonify({'flagged_wheels': flagged_wheels})


def get_trajectory_array():
    array = []
    train = load_data()
    return str(train)
    # array.append(['Age', 'Weight'])
    # for train in range(len(trains)):
    #     array.append([train['pan_size'], train['since']])
