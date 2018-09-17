#!/usr/bin/env python
#-*-coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


engine = create_engine("mysql+pymysql://img_label:r0$ett@05@10.10.198.186:3306/img_label", echo=True)

DBSession = sessionmaker(bind=engine)

# 插入
session = DBSession()
new_user_1 = User(id=13, name='xingxing')
session.add(new_user_1)
new_user_2 = User(12, 'yueliang')
session.add(new_user_2)
session.commit()
session.close()

# 查询
session = DBSession()
user = session.query(User).filter(User.id == 12).one()
print 'object======', user
print 'type======', type(user)
print 'id======', user.id
print 'name======', user.name
session.close()

