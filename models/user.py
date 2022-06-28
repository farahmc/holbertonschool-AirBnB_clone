#!/usr/bin/python3
from models.base_model import BaseModel
""" Module for class User """


class User(BaseModel):
    """
    Class User that imports from BaseModel

    Attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
