import datetime
import time
from functools import wraps


from application.config import logger, hostname, venv_name, MySQLConfig


def server_start_info():
    welcome_str = r'''
            🕸 🕸 🕸 🕸 🕸 🕸 程序已启动 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸
                        主机: {hostname}
                        Python环境: {venv_name}
                        数据库: {database}
                        启动时间: {login_time}
            🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸 🕸
            '''.format(
        hostname=hostname,
        venv_name=venv_name,
        database=MySQLConfig.database,
        login_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    logger.warning(welcome_str)




def sleephere(t):
    logger.info(f'缓冲{t}秒')
    for i in range(t):
        print(t - i)
        time.sleep(1)


def timer(func):
    @wraps(func)  # 修正 docstring
    def wrap(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        duration = et - st
        logger.warning(f'耗时{duration}秒')
        return result

    return wrap
