import unittest
import sys
from core.drinkClass import Drink
from core.peopleClass import Person
from core.roundClass import Round, roundFlag
from core.utils import clearScreen
from core.menuSelect import Selection, app
from core.dbManager import DB, db
from unittest.mock import MagicMock, patch

class TestMethods(unittest.TestCase):
    def test_people(self):
        test_person = Person("Elliot","25","Male","Blue","Black","Cyber Security")
        comparison_person_fn = "Elliot"
        comparison_person_ag = "25"
        comparison_person_ge = "Male"
        comparison_person_ec = "Blue"
        comparison_person_hc = "Black"
        comparison_person_oc = "Cyber Security"

        self.assertEqual(test_person.name, comparison_person_fn)
        self.assertEqual(test_person.age, comparison_person_ag)
        self.assertEqual(test_person.gender,comparison_person_ge)
        self.assertEqual(test_person.eyeColour,comparison_person_ec)
        self.assertEqual(test_person.hairColour,comparison_person_hc)
        self.assertEqual(test_person.occupation, comparison_person_oc)

    def test_drinks(self):
        test_drink=Drink("Hooch",True,True,"Cloudy","500")
        comparison_drink_na = "Hooch"
        comparison_drink_fi = True
        comparison_drink_al = True
        comparison_drink_co = "Cloudy"
        comparison_drink_me = "500"

        self.assertEqual(test_drink.name, comparison_drink_na)
        self.assertEqual(test_drink.isFizzy, comparison_drink_fi)
        self.assertEqual(test_drink.isAlcholic,comparison_drink_al)
        self.assertEqual(test_drink.colour,comparison_drink_co)
        self.assertEqual(test_drink.measurement,comparison_drink_me)

if __name__ == "__main__":

    unittest.main()

    