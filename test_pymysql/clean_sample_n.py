#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "CZJ"

import sys
import pymysql
import contextlib

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def conn2mysql(host='10.10.198.186',
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
        conn.commit()
        cursor.close()
        conn.close()


def select_all(table_name):
    sql = "select * from %s" % table_name
    print sql
    with conn2mysql() as cursor:
        row_count = cursor.execute(sql)
        res = []
        for i in range(row_count):
            row = cursor.fetchone()
            res.append(row)
        return res


def select_by_id(table_name, id):
    sql = "select * from %s where id=%s" % (table_name, id)
    print sql
    with conn2mysql() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
        return row


def update_by_id(table_name, columns, id):
    # deal with columns to update
    if columns is None or len(columns) == 0:
        print("Columns is None or len(columns) <= 1")
        return
    update_columns = ""
    for key, value in columns.iteritems():
            update_columns = update_columns + key + "=" + sql_value_format(value) + ","
    update_columns = update_columns.strip(',')
    # deal with sql
    sql = "update %s set %s where id=%s" % (table_name, update_columns, id)
    print sql
    with conn2mysql() as cursor:
        cursor.execute(sql)


def update_where_condition(table_name, columns, where_conditions=None):
    # deal with columns to update
    update_columns = ""
    if columns is None or len(columns) == 0:
        print("Columns is None or len(columns) == 0")
        return
    else:
        for key, value in columns.iteritems():
                update_columns = update_columns + key + "=" + sql_value_format(value) + ","
        update_columns = update_columns.strip(',')
    # deal with where condition
    where_clause = ""
    if where_conditions is not None and len(where_conditions) >= 1:
        where_clause = "where " + where_conditions[0]
        for i in range(1, len(where_conditions)):
            where_clause = where_clause + " and " + where_conditions[i]
    # deal with sql
    sql = "update %s set %s %s" % (table_name, update_columns, where_clause)
    sql = sql.strip()
    print sql
    with conn2mysql() as cursor:
        cursor.execute(sql)


def insert(table_name, columns):
    if columns is None or len(columns) == 0:
        print("Columns is None or len(columns) == 0")
        return
    keys = ""
    values = ""
    for key, value in columns.iteritems():
        keys = keys + key + ","
        if isinstance(value, str):
            values = values + "\'" + value + "\',"
        elif is_number(str(value)):
            values = values + str(value) + ","
        else:
            print("Input is not valid")
            return
    keys = keys.strip(',')
    values = values.strip(',')

    sql = "insert into %s(%s) value(%s)" % (table_name, keys, values)
    print sql
    with conn2mysql() as cursor:
        cursor.execute(sql)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


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


if __name__ == '__main__':

    for theme_id in range(2, 41):
        table_name = "sample_%d" % theme_id
        columns = {}
        columns["sample_label"] = ""
        update_where_condition(table_name, columns)
        
    # s = ",yyyyyy ,"
    # s = s.strip(', ')
    # print s

    # s = "num:"
    # for i in range(100, 10):
    #     s = s + str(i) + ","
    # print s.strip(',')



