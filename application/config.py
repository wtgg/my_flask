import os
import socket
from loguru import logger as lg

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

LOG_FILE = os.path.join(ROOT_DIR, 'flask_demo.log')

hostname = socket.gethostname()
env = dict(os.environ)
venv_name = env.get('VIRTUAL_ENV').split('/')[-1]


class MySQLConfig:
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'root'
    database = 'flask_demo'
    charset = 'utf8mb4'


if hostname == 'msi':
    MySQLConfig.port = 3336
    MySQLConfig.password = 'wtgg@msi'



SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'.format(
    user=MySQLConfig.user,
    password=MySQLConfig.password,
    host=MySQLConfig.host,
    port=MySQLConfig.port,
    database=MySQLConfig.database,
    charset=MySQLConfig.charset
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False
JSON_SORT_KEYS = False
TEMPLATES_AUTO_RELOAD = True
DATABASE_CONNECT_OPTIONS = {}

lg.add(
    LOG_FILE,
    level='DEBUG',
    # format='【{time:YYYY-MM-DD HH:mm:ss} {level} {file} {line}】{message}',
)
logger = lg


class Application:
    version = '0.0.1'
    author = 'wtgg'
    email = 'wtlit@qq.com'
    description = '这是一个flask的demo'
