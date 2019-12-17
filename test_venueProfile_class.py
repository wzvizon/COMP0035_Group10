# Weizheng Zhang
# ID: 16081188

from unittest import TestCase
from venueProfile_class import VenueProfile

class TestVenueProfile(TestCase):
    def test_capacity_is_not_a_number_larger_than_0(self):
        with self.assertRaises(TypeError):
            test_venue1 = VenueProfile('University College London','ten thousand',3)
        with self.assertRaises(ValueError):
            test_venue2 = VenueProfile('University College London', 0, 3)

    def test_type_is_not_in_the_range(self):
        with self.assertRaises(ValueError):
            test_venue3 = VenueProfile('University College London',10000,100)

if __name__ == "__main__":
    unittest.main()