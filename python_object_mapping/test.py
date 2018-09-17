#!/usr/bin/python
# -*- coding: utf-8 -*-

# python Json 对象映射
# https://www.jianshu.com/p/61ed6828faff

import json
import functools


# json->object 映射函数（不支持函数方法成员）
def __praseObject(jsonStr, Class):
    """Class needs a constructor with no arguments"""

    data = json.loads(jsonStr)
    result = Class()
    result.__dict__ = data
    return result

# 绑定函数
json.fromObject = functools.partial(json.dumps, default=lambda obj: obj.__dict__)
json.toObject = __praseObject


# Example code
class Student(object):
    def __init__(self, name="", age=0):
        super().__init__()
        self.name = name
        self.age = age

student = Student("wavky", 18)

# student -> json
jsonStr = json.fromObject(student)
print jsonStr

# json -> student
newStudent = json.toObject(jsonStr, Student)
print newStudent

