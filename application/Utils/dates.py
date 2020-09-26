import datetime
import time


class DT:

    @staticmethod
    def date2ts(date):
        '''
        :param date: <class 'datetime.date'> 类型, 形如 2018-08-12
        或者 <class 'str'> 类型 形如 '2018-08-12'
        :return: <class 'int'> 类型 形如 1534003200
        '''
        datestr_format = "%Y-%m-%d"
        timeArray = None
        if isinstance(date, datetime.date):
            timeArray = time.strptime(date.strftime(datestr_format), datestr_format)
        elif isinstance(date, str):
            timeArray = time.strptime(date, datestr_format)
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    @staticmethod
    def ts2ds(timeStamp):
        '''
        :param timeStamp:  int 时间戳， 形如：1534052846
        :return: datestr str 形如："2018-08-12"
        '''
        timeArray = time.localtime(timeStamp)
        datestr = time.strftime("%Y-%m-%d", timeArray)
        return datestr

    @staticmethod
    def ts2dts(timeStamp):
        '''
        时间戳 -> 年-月-日 时:分:秒
        :param timeStamp,  int 时间戳， 形如：1534052846
        :return: dts, str 形如："2018-08-12 13:47:26"
        '''
        dts_format = "%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(timeStamp)
        dts = time.strftime(dts_format, timeArray)
        return dts

    @staticmethod
    def ds2ts(datestr):
        '''
        :param datestr: 日期字符串 形如： "2020-07-06"
        :return: int 时间戳 形如：1593964800
        '''
        datestr_format = "%Y-%m-%d"
        timeArray = time.strptime(datestr, datestr_format)
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    @staticmethod
    def date_str2date(date_str):
        '''
        :param datestr: 日期字符串 形如： "2020-07-06"
        :return: date <class 'datetime.date'>  形如 2020-07-06
        '''
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        return date

    # 日期时间字符串转时间戳
    @staticmethod
    def dt2ts(dts):
        '''
        :param dts:  datetime 字符串，形如："2020-07-06 14:31:34"
        :return:  int 时间戳 形如：1594017094
        '''
        if isinstance(dts, datetime.datetime):
            dts = str(dts)
        dts_format = "%Y-%m-%d %H:%M:%S"
        timeArray = time.strptime(dts, dts_format)
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    @staticmethod
    def get_the_date_from_a_date(date_str, days_delta=0):
        '''比如获取2019-07-23这一天之后days_delta天的日期'''
        year, month, day = [int(i) for i in date_str.split('-')]
        date = datetime.datetime(year, month, day)
        result_date = date + datetime.timedelta(days=days_delta)
        date_str = result_date.strftime('%Y-%m-%d')
        return date_str

    @staticmethod
    def today():
        '''返回值类型<class 'datetime.date'>'''
        today = datetime.date.today()
        return today

    @staticmethod
    def tomorrow():
        '''返回值类型<class 'datetime.date'>'''
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        return tomorrow

    @staticmethod
    def yesterday():
        '''返回值类型<class 'datetime.date'>'''
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        return yesterday

    @staticmethod
    def datediff(beginDatestr, endDatestr):
        '''参数类型:str, 返回值类型: int'''
        format = "%Y-%m-%d"
        bd = datetime.datetime.strptime(beginDatestr, format)
        ed = datetime.datetime.strptime(endDatestr, format)
        days = (bd - ed).days
        return days

    # 时间戳转日期
    @staticmethod
    def timestamp2datetime(timestamp, format='ys'):
        """
        将int 类型的timeStamp,eg:1571234123
        转为str类型的时间字符串,eg:2019-10-16 21:55:23
        """
        time_local = time.localtime(timestamp)
        datetime = ''
        if format == 'ys':
            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        elif format == 'yd':
            datetime = time.strftime("%Y-%m-%d", time_local)
        elif format == 'hs':
            datetime = time.strftime("%H:%M:%S", time_local)
        return datetime

    @staticmethod
    def get_timestamp_of_today():
        today = datetime.date.today()
        timeArray = time.strptime(str(today), "%Y-%m-%d")
        timestamp = int(time.mktime(timeArray))
        return timestamp

    @staticmethod
    def now_time_str(date_format="%Y%m%d%H%M%S"):
        now = int(time.time())
        time_local = time.localtime(now)
        str = time.strftime(date_format, time_local)
        return str  # 20190806103523

    @staticmethod
    def trans_date(date_str='20080101'):
        '''
        :param date_str: 字符串类型
        :return: 字符串类型
        '''
        y = date_str[:4]
        m = date_str[4:6]
        d = date_str[-2:]
        date = '-'.join([y, m, d])
        return date

    @staticmethod
    def now_time():
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 当前时刻
        return now_time


if __name__ == '__main__':
    timeStamp = 1534052846
    datestr = DT.ts2ds(timeStamp)
    dts = DT.ts2dts(timeStamp)
    ds = DT.now_time()
    print(ds, 66666666666)
