from flask import Blueprint

from application import api
from application.views import (
    Index,
    ClassAdd,
    StudentDetail,
    StudentAdd,
    StudentDel,
    StudentHide,
    StudentList
)

index_bp = Blueprint('index', __name__)

api.add_resource(Index, "/")  # 检测app是否正常
api.add_resource(ClassAdd, "/class/add")  # 添加班级
api.add_resource(StudentAdd, "/class/<cid>/student/add")  # 添加学生  增
api.add_resource(StudentDel, "/student/delete/<sid>")  # 删除学生  删
api.add_resource(StudentHide, "/student/hide/<sid>")  # 隐藏一条数据  改
api.add_resource(StudentDetail, "/student/<sid>")  # 查看学生信息  查
api.add_resource(StudentList, "/class/<cid>/students")  # 查看某班所有学生



