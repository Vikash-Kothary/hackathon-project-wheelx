#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
models.py -
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Base(db.Model):
    """Base data model for all objects
    """
    __abstract__ = True

    def json(self):
        """Define a base way to jsonify models, dealing with datetime objects
        """

    def __repr__(self):
        return ''


class Wheels(Base):
    """Model for wheels"""

    __tablename__ = 'wheels_table'

    wheel_id = db.Column(db.Integer, primary_key=True, nullable=False)

    unit = db.Column(db.String(6))
    vehicle = db.Column(db.String(5))
    serial_no = db.Column(db.String(15))
    description = db.Column(db.String(100))
    axle_position = db.Column(db.String(1))
    measure_date = db.Column(db.String(10))
    pan_size = db.Column(db.DECIMAL)
    since = db.Column(db.DECIMAL)
    # target_date = db.Column(db.)
    # flag = db.Column(db.Boolean)

    def get_target_date():
        if unit.substring(0, 2) == "221":
            days_per_mm = 100000 / 850
            last_turn = 823
        else:  # if 220
            days_per_mm = 100000 / 750
            last_turn = 743
        days_left = (pan_size - last_turn) * days_per_mm
        return measure_date + days_left

#     def __init__(self, unit_code, vehicle_code, serial_no, description, axle_position):
#         """
#         >>> Trains(220)
#         """
#         self.unit = unit_code
#         self.vehicle = vehicle_code
#         self.serial_no = serial_no
#         self.description = description
#         self.axle_position = axle_position
#         self.flag = False


# class Schedule(Base):

#     __tablename__ = "mv_schedule"
#     unit = db.Column()
#     exam_date = db.Column()


def set_up_schedule(self):
    today = datetime.now
    for i in range(len(trains)):
        # TODO: check units are distinct
        exam = Schedule(trains['unit'], today + i)
    for i in range(len(trains)):
        check_needs_wheels()


def check_needs_wheels(self):
    # Get train by unit
    if train['target_date'] - schedule['exam_date'] < 90:
        train['flag'] = True
    else:
        schedule['exam_date'] += 90  # days


def load_data():
    import csv
    spamReader = csv.reader(open('static/trajectory.csv', newline=''), delimiter=',', quotechar='|')
    strong = ""
    for row in spamReader:
        strong += row[7] + '|' + row[6] + '#'
    return strong[:-1]


if __name__ == '__main__':
    # app = Flask(__name__)
    # db.init_app(app
    # db.create_all()
    # app.run(ip='0.0.0.0')
    load_data()
    pass
