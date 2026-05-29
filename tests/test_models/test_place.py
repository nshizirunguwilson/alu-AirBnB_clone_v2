#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ city_id attribute accepts a string value """
        new = self.value()
        new.city_id = "some_city_id"
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ user_id attribute accepts a string value """
        new = self.value()
        new.user_id = "some_user_id"
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ name attribute accepts a string value """
        new = self.value()
        new.name = "My little house"
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ description attribute accepts a string value """
        new = self.value()
        new.description = "cozy"
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ number_rooms attribute accepts an int value """
        new = self.value()
        new.number_rooms = 4
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ number_bathrooms attribute accepts an int value """
        new = self.value()
        new.number_bathrooms = 2
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ max_guest attribute accepts an int value """
        new = self.value()
        new.max_guest = 10
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ price_by_night attribute accepts an int value """
        new = self.value()
        new.price_by_night = 300
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ latitude attribute accepts a float value """
        new = self.value()
        new.latitude = 37.773972
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ longitude attribute accepts a float value """
        new = self.value()
        new.longitude = -122.431297
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ amenity_ids is a list """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
