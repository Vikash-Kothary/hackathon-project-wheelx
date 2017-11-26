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
from models import load_data, load_schedule


@app.route('/wheel_sets', methods=['GET'])
def view_all_wheel_sets():
    return jsonify({'wheel_sets': get_wheel_sets()})


def get_wheel_sets():
    return load_data()
# return render_template('view_all.html', parts=parts.query.all())


def get_schedule():
    return load_schedule()


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


@app.route('/flagged_wheels', methods=['GET'])
def get_flagged_wheels():
    return [wheel for wheel in get_wheel_sets() if not wheel['flag']]
    # TODO: Natural join schedule and wheels
    #     return jsonify({'flagged_wheels': flagged_wheels})


def get_trajectory_array():
    import csv
    spamReader = csv.reader(open('static/trajectory.csv', newline=''), delimiter=',', quotechar='|')
    strong = ""
    for row in spamReader:
        strong += row[7] + '|' + row[6] + '#'
    return strong[:-1]


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
