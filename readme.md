# flask_demo

先参照config.py创建数据库
修改MySQLConfig类中的数据库信息

`python -m venv <虚拟环境名称>` 创建虚拟环境
`source <虚拟环境路径>/bin/activate`  进入虚拟环境
`pip install -r pips.txt`
安装依赖
在根目录下执行   `gunicorn -w 1 --threads 8 -t 1200 -b 0.0.0.0:5000 run:app`
启动flask
接口在 apis.py文件中
