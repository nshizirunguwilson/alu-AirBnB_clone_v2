#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ state_id attribute accepts a string value """
        new = self.value()
        new.state_id = "some_state_id"
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ name attribute accepts a string value """
        new = self.value()
        new.name = "San Francisco"
        self.assertEqual(type(new.name), str)
