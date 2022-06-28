#!/usr/bin/python3
"""
Write a class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        if kwargs is not empty, conert created_at and updated_at string into datetime obejct
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at =datetime.strptime(kwargs["created_at"],
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at =datetime.strptime(kwargs["updated_at"],
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
