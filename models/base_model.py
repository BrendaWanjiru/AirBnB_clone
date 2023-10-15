#!/usr/bin/python3

"""Module defining all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Defines common attributes/methods for other classes
        Public Instance Attributes:
            id: (string) - assigned with a uuid when an instance is created.
            created_at: (dtatetime) - assigned with the current datetime when
                        an instance is created
            updated_at: (datetime) - assigned with current datetime when an
                                    instance is created and will be updated
                                    every time the object changes
            __str__: prints: [<class name>] (<self.id>) <self.__dict__>

        Public Instance Methods:
            save(self): updates the public instance attribute updated_at with
                        the current datetime
            to_dict(self): returns a dictionary containing all keys/values of
                            __dict__ of the instance.
    """
    def __init__(self, *args, **kwargs):
        """ Instantiate objects """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            t_form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, t_form))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """ Returns a formatted string """
        return "[{}] ({}) {}".format(self.__class__.name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the
            current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of
            of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
