#-*- coding:utf-8 -*-

from models import User,Blog,Comment
import asyncio,uuid,time
import random
from orm import Model,StringField,IntegerField

class User(Model):

	__table__ = 'users'

	id = IntegerField(primary_key=True)
	name = StringField()