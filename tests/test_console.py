#!/usr/bin/python3
"""Unittests for the HBNB command interpreter (create with parameters)."""
import unittest
from os import getenv
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
                 "create with parameters is only tested with FileStorage")
class TestConsoleCreate(unittest.TestCase):
    """Test the do_create parameter parsing feature."""

    def _create(self, line):
        """Run a create command and return the printed id."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd(line)
        return out.getvalue().strip()

    def test_create_missing_class(self):
        """create with no class prints an error."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create")
        self.assertEqual(out.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """create with an unknown class prints an error."""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create DoesNotExist")
        self.assertEqual(out.getvalue().strip(), "** class doesn't exist **")

    def test_create_string_param(self):
        """A string param has underscores replaced by spaces."""
        obj_id = self._create('create State name="My_little_house"')
        obj = storage.all()['State.' + obj_id]
        self.assertEqual(obj.name, "My little house")

    def test_create_escaped_quote(self):
        """An escaped double quote inside a string is kept."""
        obj_id = self._create('create State name="a\\"b"')
        obj = storage.all()['State.' + obj_id]
        self.assertEqual(obj.name, 'a"b')

    def test_create_int_param(self):
        """An integer param is parsed as int."""
        obj_id = self._create('create Place number_rooms=4')
        obj = storage.all()['Place.' + obj_id]
        self.assertEqual(obj.number_rooms, 4)
        self.assertIs(type(obj.number_rooms), int)

    def test_create_float_param(self):
        """A float param is parsed as float."""
        obj_id = self._create('create Place latitude=37.77')
        obj = storage.all()['Place.' + obj_id]
        self.assertEqual(obj.latitude, 37.77)
        self.assertIs(type(obj.latitude), float)

    def test_create_negative_float(self):
        """A negative float param is parsed correctly."""
        obj_id = self._create('create Place longitude=-122.43')
        obj = storage.all()['Place.' + obj_id]
        self.assertEqual(obj.longitude, -122.43)

    def test_create_skips_bad_param(self):
        """A malformed param is skipped, the rest are kept."""
        obj_id = self._create('create State name="ok" badtoken =alsobad')
        obj = storage.all()['State.' + obj_id]
        self.assertEqual(obj.name, "ok")
        self.assertFalse(hasattr(obj, 'badtoken'))

    def test_create_unclosed_string_skipped(self):
        """An unterminated string value is skipped."""
        obj_id = self._create('create State name="oops')
        obj = storage.all()['State.' + obj_id]
        self.assertFalse(hasattr(obj, 'name') and obj.name == 'oops')


if __name__ == "__main__":
    unittest.main()
