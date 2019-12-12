#Placeholder class to show how inheritance with musicianProfile works
class userProfile(object):
    def __init__(self):
        pass

class musicianProfile(userProfile):
    """Represents a Musician which inherits from userProfile."""

    ## Constants used for validation
    MINIMUM_LENGTH = 3
    MAXIMUM_LENGTH = 20

    MINIMUM_STATUS = 0
    MAXIMUM_STATUS = 1

    def __init__(self, music_instrument, group_status, exp):
        """
        Constructor for the musicianProfile class.

        :param str music_instrument: The instrument e.g. Vocals.
        :param int group_status: Integer showing group status.
        :param str exp: Text explaining experience.
        """
        self.music_instrument = music_instrument
        self.group_status = group_status
        self.experience = exp

    #string representation
    def __str__(self):
        if self.group_status == 1:
            _group_str = "In a group"
        else:
            _group_str = "Not in a group"
        return "\nInstrument: {} \nGroup status: {} \nExperience: {}"\
            .format(self.music_instrument, _group_str, self.experience)

    # Instrument setter and checker
    @property
    def music_instrument(self):
        """Defines the instrument"""
        return self._music_instrument

    @music_instrument.setter
    def music_instrument(self, inst):
        """Parses the instrument input to check its valid"""
        try :
            self.is_valid_string(inst)
            self._music_instrument = inst
        except ValueError as err :
            raise
            self._music_instrument = inst

    # Experience setter and checker
    @property
    def experience(self):
        """Defines experience"""
        return self._experience

    @experience.setter
    def experience(self, exp):
        """Parses the experience input to check its valid"""
        try :
            self.is_valid_string(exp)
            self._experience = exp
        except ValueError as err :
            raise
            self._experience = exp

    #Group status setter and checker
    @property
    def group_status(self):
        """Defines group status"""
        return self._group_status

    @group_status.setter
    def group_status(self, status):
        """Parses the group status input to check its valid"""
        try:
            status = int(status)
            self.is_valid_status(status)
            self._group_status = (status)
        except ValueError as err :
            raise
            self._group_status = _stat_int


    # Methods for validating string inputs
    @staticmethod
    def is_valid_string(string):
        """Checks strings are within defined length and are alphanumeric """
        if len(string) > musicianProfile.MAXIMUM_LENGTH \
            or len(string) < musicianProfile.MINIMUM_LENGTH :
            raise ValueError\
            (("{}, is not valid. It should be: " +
                         "more than {} characters long " +
                         "and less than {} characters long.")
                .format(string, musicianProfile.MINIMUM_LENGTH - 1,\
                        musicianProfile.MAXIMUM_LENGTH + 1))

        for chr in string :
            if not all(chr.isalpha() or chr.isspace() for chr in string):
               raise ValueError\
                (("{}, is not valid. All characters should be " +
                                 "alphanumeric.").format(string))
        return True

    # Methods for validating integer status inputs
    @staticmethod
    def is_valid_status(stat):
        """Checks group status is in the correct format"""
        if stat > musicianProfile.MAXIMUM_STATUS \
                or stat < musicianProfile.MINIMUM_STATUS:
            raise ValueError \
                (("{}, is not valid. It should be " +
                  "in the range between {}" +
                  "and {}.")
                 .format(int, musicianProfile.MINIMUM_STATUS,\
                         musicianProfile.MAXIMUM_STATUS))
        return True

if __name__ == "__main__":
    userProfile = 1
    a1 = musicianProfile("Vocals", "0" , "Not much")
    a2 = musicianProfile("Drum kit", "a", "More than you")
    print(a1)
    print(a2)
