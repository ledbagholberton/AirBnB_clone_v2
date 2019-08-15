#!/usr/bin/python3
"""test for db storage"""
import unittest
import pep8
import os
import console
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import MySQLdb
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @classmethod
    def setUpEnv(self):
        """set up environmental variables"""
        os.environ["HBNB_ENV"]="dev"
        os.environ["HBNB_MYSQL_USER"]="hbnb_dev"
        os.environ["HBNB_MYSQL_PWD"]="hbnb_dev_pwd"
        os.environ["HBNB_MYSQL_DB"]="hbnb_dev_db"
        os.environ["HBNB_TYPE_STORAGE"]="db"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.export("HBNB_ENV=test")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in DBStorage"""
        db = MySQLdb.connect(
        host="localhost",
        user="hbnb_dev",
        passwd="hbnb_dev_pwd",
        db="hbnb_dev_db",
        port=3306)
        cursor = db.cursor()
        os.environ["HBNB_ENV"]="db"
        console.raw_input = lambda _: 'create State name="California"'
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    def test_new(self):
        """test when new is created"""
        db = MySQLdb.connect(
        host="localhost",
        user="hbnb_dev",
        passwd="hbnb_dev_pwd",
        db="hbnb_dev_db",
        port=3306)
        os.environ["HBNB_ENV"]="db"
        cursor = db.cursor()
        a = cursor.execute("SELECT * FROM states")
        console.raw_input = lambda _: 'create State name="California"'
        b = cursor.execute("SELECT * FROM states")
#        cursor.close()
        self.assertEqual(a + 1, b)

    def test_reload_dbstorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
