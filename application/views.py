from flask import make_response, jsonify, request
from flask_restful import Resource

from application import db
from application.Utils.dates import DT
from application.common import timer
from application.config import logger
from application.models import ClassInstance, Student


class Index(Resource):

    def get(self):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        now_time = DT.now_time()  # 当前时刻

        msg = f'index 请求成功！ {now_time}'
        logger.warning(msg)

        status_code = 200
        return make_response(
            jsonify(
                dict(
                    status_code=status_code,
                    msg=msg
                )
            ), status_code
        )


class ClassAdd(Resource):

    def post(self):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        post_data = request.form
        name = post_data.get('name')
        class_instance = ClassInstance()
        class_instance.name = name
        db.session.add(class_instance)
        db.session.commit()
        msg = f'添加成功！'
        logger.success(msg)

        status_code = 200
        return make_response(
            jsonify(
                dict(
                    status_code=status_code,
                    msg=msg
                )
            ), status_code
        )


class StudentAdd(Resource):

    def post(self, cid):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        post_data = request.form
        name = post_data.get('name')
        gender = post_data.get('gender')
        birthday = post_data.get('birthday')

        if gender == '男':
            gender = 1
        else:
            gender = 0
        student = Student()
        student.cid = int(cid)
        student.name = name
        student.gender = gender
        try:
            birthday_date = DT.date_str2date(birthday)
            student.birthday = birthday_date
            db.session.add(student)
            db.session.commit()
            msg = f'添加成功！'
            logger.success(msg)
            status_code = 200
            return make_response(
                jsonify(
                    dict(
                        status_code=status_code,
                        msg=msg
                    )
                ), status_code
            )
        except Exception as e:
            msg = f'error:{e} \n请按照 2001-01-01的格式输入生日'
            logger.error(msg)
            status_code = 400
            return make_response(
                jsonify(
                    dict(
                        status_code=status_code,
                        msg=msg
                    )
                ), status_code
            )


class StudentDel(Resource):

    def delete(self, sid):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        student = Student.query.filter(
            Student.id == int(sid)
        ).first()
        db.session.delete(student)
        db.session.commit()
        msg = '删除成功！'
        logger.success(msg)
        status_code = 200
        return make_response(
            jsonify(
                dict(
                    status_code=status_code,
                    msg=msg
                )
            ), status_code
        )


class StudentHide(Resource):

    def put(self, sid):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        student = Student.query.filter(
            Student.id == int(sid)
        ).first()
        student.is_deleted = 1
        db.session.commit()
        msg = '修改成功！'
        logger.success(msg)
        status_code = 200
        return make_response(
            jsonify(
                dict(
                    status_code=status_code,
                    msg=msg
                )
            ), status_code
        )


class StudentDetail(Resource):

    @timer
    def get(self, sid):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        student = Student.query.filter(
            Student.id == int(sid)
        ).first()
        age = (DT.today() - student.birthday).days // 365
        data = dict(
            name=student.name,
            age=age,
            gender='男' if student.gender else '女'
        )
        status_code = 200
        return make_response(
            jsonify(data), status_code
        )


class StudentList(Resource):

    @timer
    @logger.catch()
    def get(self, cid):
        logger.debug(f"{str(request).replace(request.url_root, '/')}")
        students = Student.query.join(
            ClassInstance,
            ClassInstance.id == Student.cid
        ).filter(
            ClassInstance.id == int(cid),
            Student.is_deleted == 0
        ).all()

        rows = [
            dict(
                name=student.name,
                age=(DT.today() - student.birthday).days // 365,
                gender='男' if student.gender else '女'
            ) for student in students
        ]
        status_code = 200
        return make_response(
            jsonify(rows), status_code
        )
