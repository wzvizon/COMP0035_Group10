from unittest import TestCase
from group_profile_class import group_profile_class

class Test_group_profile(TestCase):
    def test_invite_artist(self):
        self.group_profile_test_case = group_profile_class("Holloway's Finest", ["1", "2"])
        self.group_profile_test_case.invite_artist(self.group_profile_test_case.contributing_artists,"3")
        self.assertEqual(len(self.group_profile_test_case.contributing_artists),4)
        print(self.group_profile_test_case.contributing_artists)

def main():
    group_test_setup = Test_group_profile()
    group_test_invite = group_test_setup.test_invite_artist()


if __name__ == '__main__':
    main()