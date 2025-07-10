from flask import Flask, request, jsonify
# import os
# from openpyxl import Workbook, load_workbook
from db import init_db,creat_data, query_db
from models.students import Student
from models.teachers import Teacher

app = Flask(__name__)

# POST 接口：/api/student
@app.route('/api/student', methods=['POST'])
def create_student():
    data = request.get_json()  # 获取 JSON 请求体
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    email = data.get('email', '')  # 可选字段，默认为空字符串
    creat_state =  creat_data.create_student_by_orm(name, gender, age, email)

    if creat_state is False:
        return jsonify({
            "message": "error",
            "code": 500,
            "data": None
        }), 500
    
    # # 这里需要将这些内容写到studen xls中
    # # 需要判断students.xls 是否存在
    # if not os.path.exists('students.xlsx'):
    #     # 如果文件不存在，创建一个新的Excel文件
    #     workbook = Workbook()
    #     worksheet = workbook.active
    #     worksheet.append(['Name', 'Age', 'Gender'])  # 添加表头
    # else:
    #     # 如果文件存在，打开它
    #     workbook = load_workbook('students.xlsx')
    #     worksheet = workbook.active

    # # 将学生信息写入Excel
    # worksheet.append([name, age, gender])
    # workbook.save('students.xlsx')

    # 模拟保存或处理逻辑
    return jsonify({
        "message": "ok",
        "code": 200,
        "data": {
            "name": name,
            "age": age,
            "gender": gender,
            "email": email
        }
    }), 201

@app.route('/api/students', methods=['GET'])
def get_all_students():
    students = Student.all_students()
    # 模拟从数据库或其他存储中获取所有学生信息
    # students = query_db.get_all_students()

    if not students:
        return jsonify({
            "message": "error",
            "code": 404,
            "data": None
        }), 404
    print(students)
    # 将学生信息转换为字典列表
    # results = [dict(row) for row in students]
    # 如果使用 ORM 模型，直接转换为字典列表
    print(students)
    results = []
    for student in students:
        results.append(student.to_dict())
    return jsonify({
        "message": "ok",
        "code": 200,
        "data": results
    })

@app.route('/api/student/<name>', methods=['GET'])
def get_student_by_name(name):
    student = Student.with_name(name)

    if not student:
        return jsonify({
            "message": "error",
            "code": 404,
            "data": None
        }), 404
    
    return jsonify({
        "message": "ok",
        "code": 200,
        "data": student.to_dict()
    }), 200

@app.route('/api/student/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = Student.with_id(student_id)

    if not student:
        return jsonify({
            "message": "error",
            "code": 404,
            "data": None
        }), 404
    
    return jsonify({
        "message": "ok",
        "code": 200,
        "data": student.to_dict()
    }), 200

@app.route('/api/student/with_email', methods=['GET'])
def get_student_by_email():
    email = request.args.get('email')
    student = Student.with_email(email)

    if not student:
        return jsonify({
            "message": "error",
            "code": 404,
            "data": None
        }), 404

    return jsonify({
        "message": "ok",
        "code": 200,
        "data": student.to_dict()
    }), 200

@app.route('/api/teacher', methods=['POST'])
def create_teacher():
    data = request.get_json()  # 获取 JSON 请求体
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    email = data.get('email', '')  # 可选字段，默认为空字符串

    Teacher.create_teacher(name=name, age=age, email=email, gender=gender)
    # 模拟保存或处理逻辑
    return jsonify({
        "message": "ok",
        "code": 200,
        "data": {
            "name": name,
            "age": age,
            "gender": gender
        }
    }), 201

@app.route('/api/course', methods=['POST'])
def create_course():
    data = request.get_json()  # 获取 JSON 请求体
    name = data.get('name')
    description = data.get('description')
    
    # 模拟保存或处理逻辑
    return jsonify({
        "message": "ok",
        "code": 200,
        "data": {
            "name": name,
            "description": description
        }
    }), 201

if __name__ == '__main__':
    # init database
    init_db.init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
