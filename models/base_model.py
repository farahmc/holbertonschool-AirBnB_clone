#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dttime_ob = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dttime_ob)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at public instance attribute with the current
        datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all key/values of __dict__
        """
        ret_dict = self.__dict__.copy()
        ret_dict['created_at'] = datetime.isoformat(ret_dict['created_at'])
        ret_dict['updated_at'] = datetime.isoformat(ret_dict['updated_at'])
        ret_dict['__class__'] = self.__class__.__name__
        return ret_dict
