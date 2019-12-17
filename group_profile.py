# Dillon Lad
# SN: 17053282
#This is to demonstrate how to push a new change

from unittest import TestCase
from group_profile_class import group_profile_class

class Test_group_profile(TestCase):
    def test_invite_artist(self):
        self.group_profile_test_case = group_profile_class("Holloway's Finest", ["1", "2"])
        self.group_profile_test_case.invite_artist(self.group_profile_test_case.contributing_artists,"3")
        self.assertEqual(len(self.group_profile_test_case.contributing_artists),3)
        print(self.group_profile_test_case.contributing_artists)

    def test_set_group_name(self):
        self.group_profile_test_case_two = group_profile_class("Band One", ["Marshall","Jermaine","Miles"])
        self.original_band_name = self.group_profile_test_case_two.band_name
        self.group_profile_test_case_two.set_group_name(self.group_profile_test_case_two.band_name,"Holloway's Finest")
        self.assertNotEqual(self.original_band_name,self.group_profile_test_case_two.band_name)

def main():
    group_test_setup = Test_group_profile()
    group_test_invite = group_test_setup.test_invite_artist()
    group_test_newname = group_test_setup.test_set_group_name()


if __name__ == '__main__':
    main()