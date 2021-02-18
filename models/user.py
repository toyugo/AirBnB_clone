#!/usr/bin/python3
""" Module User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User base en BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""