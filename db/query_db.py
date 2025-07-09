import sqlite3
import models.students as students_model
import models.base as db_engine
from sqlalchemy.orm import Session

def get_student_with_name(name: str):
    with Session(db_engine.engine) as session:
        student = session.query(students_model.Student).filter_by(name=name).first()
        if student:
            return {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "gender": student.gender,
                "email": student.email
            }
    return None

def get_all_students_by_orm():
    with Session(db_engine.engine) as session:
        students = session.query(students_model.Student).all()
        return students

"""
过程是这样的
1. 请求创建接口
2. 连接sqlite数据库
3. 执行inster操作
4. inster失败 可能唯一字段重复类似的问题
5. 接口报异常
6. 重复1操作 出现database is locked错误

带来一个新的问题：
1. 获取连接
2. 获取游标
3. 执行insert操作
4. conn.commit
5. conn.close()
这里的问题就是如果 我在3的时候就异常了 会执行4，5吗同样在4.的时候异常还会执行5吗
如果 不会执行 接下来有新的请求进来是不是就会出现lock的问题 

像这样的写法
    conn = sqlite3.connect('school.db', timeout=3)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    results = [dict(row) for row in rows]
    conn.close()
    if not results:
        return []
    
    return results
results = [dict(row) for row in rows]  # 将每一行转换为字典形式
在pg数据库可以实现吗
"""
"""
// 邦讯技术 13k 2016 09 - 2019 07 rails / java mysql 信息中心开发工程师
activity: 使用activiti工作流引擎,配置业务工作流
rails 开发项目管理平台

// 大连智慧比特 15k remote 2019 08 - 2020 07 rails pg nginx rails开发工程师
微信商城，ios 后端api

// 开源中国 23k 2020 08 - 2023 3 rails / golang  mysql k8s 高级开发工程师
gitee-code-server code-golang k8s 

// 智能创新中心 29k 2023 7 - 2024 6 golang python c++ mysql leveldb vue protobuf 云原生开发工程师
k3s 管理平台 client-go

智能装备集成项目 c++用于底层设备控制，mysql作为主要数据库，leveldb用于高性能数据存储

"""