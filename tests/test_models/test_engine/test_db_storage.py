#!/usr/bin/python3
""" Module for testing database storage (only relevant for db engine)."""
import unittest
from os import getenv
from models import storage
from models.state import State


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                 "DBStorage tests only relevant for db storage")
class test_dbStorage(unittest.TestCase):
    """ Class to test the database storage engine """

    def test_storage_type(self):
        """ storage is a DBStorage instance """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)

    def test_new_and_all(self):
        """ A new State is saved and retrievable via all() """
        new = State(name="California")
        new.save()
        self.assertIn('State.' + new.id, storage.all(State))

    def test_delete(self):
        """ A saved State can be deleted """
        new = State(name="Nevada")
        new.save()
        key = 'State.' + new.id
        self.assertIn(key, storage.all(State))
        storage.delete(new)
        storage.save()
        self.assertNotIn(key, storage.all(State))

    def test_all_returns_dict(self):
        """ all() returns a dictionary """
        self.assertEqual(type(storage.all()), dict)


if __name__ == "__main__":
    unittest.main()
