#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.base_model import os_type_storage


if os_type_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
