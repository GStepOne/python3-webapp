#-*- coding:utf-8 -*-
from orm import Model,StringField,BooleanField, FloatField, TextField
import time
import asyncio
import orm
import random,uuid

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)



class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key = True,default = next_id,ddl= 'varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(50)')
    content = TextField()
    created_at = FloatField(default = time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key = True,default = next_id,ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    content = TextField()
    created_at = FloatField(default=time.time)




#
# async def test_save(loop):
#     id = random.randint(1,99)
#     await orm.create_pool(loop,user="root",password="root",db="test")
#     user = User(id=id,name="jack")
#     await user.save()
#     await orm.destory_pool()
#
#
#
#
# loop = asyncio.get_event_loop()
#
# loop.run_until_complete(test_save(loop))