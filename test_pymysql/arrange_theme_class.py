#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "CZJ"
 
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
    sql = "select * from " + table_name
    print sql
    with conn2mysql() as cursor:
        row_count = cursor.execute(sql)
        res = []
        for i in range(row_count):
            row = cursor.fetchone()
            res.append(row)
        return res


def select_by_id(table_name, id):
    sql = "select * from " + table_name + " where id=" + id
    print sql
    with conn2mysql() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
        return row


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
    keys = keys[0: len(keys)-1]
    values = values[0: len(values)-1]

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


if __name__ == '__main__':

    # print is_number("23")

    # res = select_all("img_class")
    # print res[0]["name"]
    #
    # res = select_by_id("img_theme", "1")
    # print res["name"]
    #
    # columns = {}
    # columns["id"] = 126
    # columns["name"] = "test"
    # insert("img_class", columns)

    for theme_id in range(1, 41):
        sample_label_table = "sample_" + str(theme_id) + "_label"
        rows = select_all(sample_label_table)
        for row in rows:
            class_id = row["class_id"]
            print theme_id, class_id
            columns = {}
            columns["theme_id"] = theme_id
            columns["class_id"] = class_id
            insert("img_theme_class", columns)

