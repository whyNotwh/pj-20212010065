from flask import Flask
from flask import request
import flask
import db
import json
app = Flask(__name__)
# -*- coding: UTF-8 -*-

# http://127.0.0.1:5000
@app.route('/')
def index():
    return '学生信息管理系统'

# http://127.0.0.1:5000/api/v1/student
@app.route('/api/v1/student', methods=['POST', 'GET', 'DELETE', 'PUT'])
def school():
    # 添加学生
    if request.method == 'POST':
        params = flask.request.json
        if params:
            studentId = str(params.get('studentId'))
            name = params.get('name')
            department = params.get('department')
            major = params.get('major')
            sql = "INSERT INTO schoolManagement(studentId,name,department,major)VALUES('%s','%s','%s','%s')" % (
            studentId, name, department, major)
            printStr = "增添学生信息  " + sql
            db.my_db(sql)
            return printStr
    # 修改学生信息
    elif request.method == 'PUT':
        params = flask.request.json
        if params:
            studentId = str(params.get('studentId'))
            name = params.get('name')
            department = params.get('department')
            major = params.get('major')
            sql = "UPDATE schoolManagement SET name='%s', department='%s', major='%s' WHERE studentId='%s'" % (
            name, department, major, studentId)
            printStr = "更改学生信息  " + sql
            db.my_db(sql)
            return printStr
    # 查看学生信息
    elif request.method == 'GET':
        sql = "SELECT * FROM schoolManagement"
        res = db.my_db(sql)
        return json.dumps(res, ensure_ascii=False)
    # 删除学生
    elif request.method == 'DELETE':
        id = flask.request.json
        studentId = str(id.get('studentId'))
        print(studentId)
        sql = "DELETE FROM schoolManagement WHERE studentId = %s" % (studentId)
        printStr = "删除学生信息  " + sql
        res = db.my_db(sql)
        return printStr

# 启动WEB服务器
if __name__ == '__main__':
    app.run(debug=True)
