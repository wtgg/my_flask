from application import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        comment='本条数据的新增时间'
    )
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
        comment='本条数据被修改的时间'
    )


class ClassInstance(Base):
    __tablename__ = 'classes'
    name = db.Column(db.String(50), index=True, comment='班级')  #
    is_deleted = db.Column(db.Integer, default=0, index=True)  # 是否被隐藏


Female = 0
Male = 1


class Student(Base):
    __tablename__ = 'students'
    cid = db.Column(db.Integer, nullable=False, index=True)  # 是否被隐藏
    name = db.Column(db.String(50), index=True, comment='名字')  #
    gender = db.Column(db.Integer, default=Female, index=True, comment='性别')
    birthday = db.Column(db.Date, comment='生日')
    is_deleted = db.Column(db.Integer, default=0, index=True)  # 是否被隐藏
