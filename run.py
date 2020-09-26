
from application import app, initialize

initialize()
'''
运行命令: 在当前目录下

gunicorn -w 1 --threads 8 -t 1200 -b 0.0.0.0:5000 run:app

关闭5000端口的程序：
fuser -k -n tcp 5000
'''
