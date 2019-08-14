#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
import os
from models import dict_classes
from models.base_model import Base
from models.base_model import os_user, os_pass, os_host, os_db, os_env
from models.state import State
from models.city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class storage instances in MySQL
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os_user, os_pass, os_host, os_db),
                                      pool_pre_ping=True)
        if os_env == "test":
            drop_all(bind=None)


    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        print("MY CLASS", cls)
        if cls in dict_classes:
            a = self.__session.query(dict_classes[cls]).all()
            print("ESTE ES MI QUERY", a)
            #return (session.query(cls).all())
            self.__session.commit()
            self.__session.close()
        else:
            #print(self.__session.all())
            #return (session.query.all())
            print("vacio")
            self.__session.commit()
            self.__session.close()

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind = self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """Delete obj from _objects"""
        if obj:
            self.__session.delete(obj)