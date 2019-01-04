#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2019/1/4'
"""
from flask import Flask, jsonify, render_template, request
import random
from pagination import Pagination

app = Flask(__name__)

_last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']
_first_name = ['明', '红', '鑫', '军', '卫', '珊', '丽', '美']

app.config['SECRET_KEY'] = 'hard to guess key'


class Person:
    def __init__(self):
        self.name = random.choice(_last_names) + random.choice(_first_name)
        self.age = random.randint(1, 100)
        self.sex = random.choice(['男', '女'])

    @property
    def show_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'sex': self.sex
        }


_persons = [Person() for x in range(1000)]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_persons', methods=['POST'])
def get_person():
    page = request.args.get('page', 1, type=int)
    pagination = Pagination(_persons, page=page, per_page=10)
    return jsonify(pagination.get_dict())


if __name__ == '__main__':
    app.run()
