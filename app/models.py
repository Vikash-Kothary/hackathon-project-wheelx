#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
models.py -
"""

from flask_sqlalchemy import SQLAlchemy
import datetime
from dateutil.relativedelta import relativedelta

db = SQLAlchemy()


class Base(db.Model):
    """Base data model for all objects
    """
    __abstract__ = True

    def as_dict(self):
        """Define a base way to jsonify models, dealing with datetime objects
        """

    def __repr__(self):
        return ''


class WheelsDB(Base):
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
    target_date = db.Column(db.DateTime)
    flag = db.Column(db.Boolean)


class Wheels():

    def __init__(self, values):
        if isinstance(values[6], int):
            raise ValueError
        self.unit = values[0]
        self.vehicle = values[1]
        self.serial_no = values[2]
        self.description = values[3]
        self.axle_position = values[4]
        self.measure_date = values[5]  # datetime.datetime.strptime(
        self.pan_size = int(values[6])
        self.target_date = self.get_target_date()
        self.flag = False

    def get_target_date(self):
        if self.unit[0:3] == "221":
            days_per_mm = 1400000 / (850 * 61)
            last_turn = 799
        else:  # if 220
            days_per_mm = 1400000 / (750 * 61)
            last_turn = 719
        days_left = (self.pan_size - last_turn) * days_per_mm
        # return self.measure_date + days_left
        return days_left

    def as_dict(self):
        return {
            'unit': self.unit,
            'vehicle': self.vehicle,
            'serial_no': self.serial_no,
            'description': self.description,
            'axle_position': self.axle_position,
            'measure_date': self.measure_date,
            'pan_size': self.pan_size,
            'target_date': self.target_date,
            'flag': self.flag
        }


# class ScheduleDB(Base):

#     __tablename__ = "mv_schedule"
#     schedule_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     unit = db.relationship('Wheels', backref='mv_schedule', lazy=True, uselist=False)
#     exam_date = db.Column(db.DateTime)


class Schedule():

    def __init__(self, values):
        self.unit = values[0]
        self.exam_date = values[1]

    def as_dict(self):
        return {
            'unit': self.unit,
            'exam_date': self.exam_date
        }


def load_data():
    import csv
    spamReader = csv.reader(open('static/trajectory.csv', newline=''), delimiter=',', quotechar='|')
    data = []
    for row in spamReader:
        try:
            wheel = Wheels(row).as_dict()
            data.append(wheel)
        except ValueError:
            pass
    return data


def load_schedule():
    exam_date_now = datetime.date.today()
    wheels = load_data()
    return [wheel['target_date'] for wheel in wheels]
    exams = []
    for wheel in wheels:
        # TODO: check units are distinct
        exam_date_now += datetime.timedelta(days=1)
        exam = Schedule([wheel['unit'], exam_date_now])
        exams.append(exam)
    # for exam in exams:
    #    unit = (wheel for wheel in wheels if wheel['unit'] == exam.as_dict()['unit'])
    #    return check_needs_wheels(exam, unit)
    return [(wheel, exam.as_dict()['exam_date']) for wheel in wheels if wheel['flag'] == True]


def check_needs_wheels(exam, unit):
    no_flags = True
    for wheel in unit:
        rd = relativedelta(wheel['target_date'], exam.as_dict()['exam_date'])
        return rd.days
        if rd .days < 90:
            wheel['flag'] = True
            no_flags = False
    if no_flags:
        schedule['exam_date'] += 90  # days


if __name__ == '__main__':
    # app = Flask(__name__)
    # db.init_app(app
    # db.create_all()
    # app.run(ip='0.0.0.0')
    # load_data()
    pass
