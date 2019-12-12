from unittest import TestCase

from dan import musicianProfile

class TestMusicianProfile(TestCase):
    #Tests to try invalid inputs for instrument aswell as valid
    def test_music_instrument(self):
        print("\nInstrument Test A: Create instrument with Valid name")
        try:
            instrument1 = musicianProfile("Vocals", 0, "None")
            print("\tVALID Instrument: ", instrument1.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test B: Create instrument with invalid symbols")
        try:
            instrument2 = musicianProfile("Drum$$K!t", 0, "None")
            print("\tVALID Instrument: ", instrument2.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test C: Create instrument with whitespace")
        try:
            instrument3 = musicianProfile("Drum kit", 0, "None")
            print("\tVALID Instrument: ", instrument3.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test D: Create instrument that is too short")
        try:
            instrument4 = musicianProfile("An", 0, "None")
            print("\tVALID Instrument: ", instrument4.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test E: Create instrument that is too long")
        try:
            instrument5 = musicianProfile("A really long instrument", 0, "None")
            print("\tVALID Instrument: ", instrument5.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

    # parser same as instrument so no need to test right now
    def test_experience(self):
        pass

    # Tests to try invalid inputs for group status aswell as valid
    def test_group_status(self):
        print("\nGroup Test A: Valid group status")
        try:
            group1 = musicianProfile("None", 0, "None")
            print("\tVALID Group: ", group1.group_status)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nGroup Test B: Non-integer group status")
        try:
            group2 = musicianProfile("None", "a", "None")
            print("\tVALID Group: ", group2.group_status)
        except Exception as err:
            print("\tERROR: ", err)
        print("\nGroup Test C: Integer out of range group status")
        try:
            group3 = musicianProfile("None", 12, "None")
            print("\tVALID Group: ", group3.group_status)
        except Exception as err:
            print("\tERROR: ", err)
