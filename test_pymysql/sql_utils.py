#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "CZJ"

import sys
import pymysql
import contextlib

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def get_connection(host='10.10.198.186',
               port=3306,user='img_label',
               passwd='r0$ett@05',
               db='img_label',
               charset='utf8'):

    conn = pymysql.connect(host=host,
                           port=port,
                           user=user,
                           passwd=passwd,
                           db=db,
                           charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    try:
        yield cursor
    finally:
        # 提交到数据库执行
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()


# 执行sql语句,无返回值
def exe(sql):
    print sql
    with get_connection() as cursor:
        cursor.execute(sql)


# 执行sql语句,有返回值
def exe(sql):
    print sql
    with get_connection() as cursor:
        row_count = cursor.execute(sql)
        res = []
        for i in range(row_count):
            row = cursor.fetchone()
            res.append(row)
        return res


# 批量执行sql语句,无返回值
# sql_format: sql格式化模板
# params: 一个tuple或者list
# 参数示例
# sql_format = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)"
# params = (('xiaoming', 31, 'boy'), ('hong', 22, 'girl'), ('wang', 90, 'man'))
def exe_many(sql_format, params):
    with get_connection() as cursor:
        cursor.executemany(sql_format, params)
    print sql_format, "执行了", len(params), "次"


# 判断是否是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


# 格式化sql数值格式
def sql_value_format(value):
    if value is None:
        print "Input is None"
        sys.exit(1)
    elif isinstance(value, str):
        if is_number(value):
            return value
        else:
            return "\'" + value + "\'"
    elif is_number(str(value)):
        return str(value)
    else:
        print("Input is not valid")
        sys.exit(1)

