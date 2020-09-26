from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from application import config

from flask_restful_swagger import swagger
from application.config import Application

app = Flask(__name__)
# 加载配置
app.config.from_object(config)
CORS(app, supports_credentials=True)  # 解决跨域问题

# swagger
api = swagger.docs(
    Api(app),
    apiVersion=Application.version,
    api_spec_url="/api",
    description=Application.description
)

db = SQLAlchemy(app=app, session_options=dict(autocommit=False, autoflush=True))


def init_database():
    from application.models import ClassInstance, Student
    db.init_app(app)
    db.create_all(app=app)



def register_blueprints(app):
    from application.apis import index_bp
    app.register_blueprint(index_bp)


def initialize():
    init_database()  # 初始化数据库
    register_blueprints(app)  # 注册蓝图和api

    from application.common import server_start_info
    server_start_info()  # 输出系统启动欢迎信息
