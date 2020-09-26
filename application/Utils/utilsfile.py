import datetime
import os
import json


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


class UtilsBox:
    # logger = getLogger(__name__)  # scrapy模块的日志,写入settings文件中定义的LOG_FILE文件中
    @staticmethod
    def mkdir(dirpath):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

    @classmethod
    def purge_string(self, instring):
        """
        去掉数据中的空格换行等字符
        :param instring:
        :return:
        """
        move = dict.fromkeys((ord(c) for c in u"\xa0\n\t|│:：<>？?\\/*’‘“”\"\x01\x02"))
        outstring = instring.translate(move)
        return outstring

    @staticmethod
    def save_text(file=None, text=None, mode='w'):
        file_path = os.path.abspath(file)
        file_dir_path = os.path.dirname(file_path)
        if not os.path.exists(file_dir_path):
            os.makedirs(file_dir_path)
        with open(file, mode=mode, encoding='utf8') as f:
            f.write(text)

    @staticmethod
    def trans_json_text_to_json(text_file_path):
        with open(text_file_path, 'r', encoding='utf8') as f:
            json_str = f.read()
        json_obj = json.loads(json_str)
        return json_obj

    @staticmethod
    def extract_from_dict(keys=[], data={}):
        '''返回data字典中包含keys字段的部分'''
        new_dict = {}
        for k in keys:
            new_dict[k] = data.get(k)
        return new_dict

    @staticmethod
    def dict_dumps(data):
        '''将字典转为字典样式的字符串,主要转换datetime类型的value'''
        return json.dumps(data, ensure_ascii=False, cls=DateEncoder)

    @staticmethod
    def dict_dumps_date_keys(data):
        new_data = {}
        for k, v in data.items():
            if 'datetime' in type(v):
                new_data[k] = str(v)
            else:
                new_data[k] = v

        return new_data


if __name__ == "__main__":
    pass
