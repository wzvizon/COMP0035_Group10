class userProfile():
    pass

class group_profile_class(userProfile):

    MINIMUM_NAME_LENGTH = 8
    MIMIMUM_GROUP_SIZE = 2
    MIMIMUM_PASSWORD_LENGTH = 8

    def __init__(self,groupName,artists):
        self.band_name = groupName
        self.contributing_artists = artists

    @property
    def band_name(self):
        return self._band_name

    @band_name.setter
    def band_name(self,groupName):
        self.validate_name(groupName)
        self._band_name = groupName

    def invite_artist(self,contributing_artists,new_member):
        self.contributing_artists.append(new_member)

    def remove_artist(self,contributing_artists, member_to_remove):
        self.contributing_artists.remove(member_to_remove)

    def set_group_name(self,band_name,new_group_name):
        self.band_name = new_group_name
        self.validate_new_name(new_group_name)

    @staticmethod
    def validate_name(band_name):
        if len(band_name) <  group_profile_class.MINIMUM_NAME_LENGTH:
            raise TypeError("Band name not long enough!")

def main():
    try:
        first_group_profile = group_profile_class("Holloway's Finest",["Marshall","Jermaine","Miles"])
        print(first_group_profile.band_name)
        print(first_group_profile.contributing_artists)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
