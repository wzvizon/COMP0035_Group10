from unittest import TestCase

from dan import musicianProfile

class TestMusicianProfile(TestCase):

    def test_music_instrument(self):
        print("\nInstrument Test A: Create instrument with Valid name")
        try:
            Instrument1 = musicianProfile("Vocals", 0, "None")
            print("\tVALID Instrument: ", Instrument1.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test B: Create instrument with invalid symbols")
        try:
            Instrument2 = musicianProfile("Drum$$K!t", 0, "None")
            print("\tVALID Instrument: ", Instrument2.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test C: Create instrument with whitespace")
        try:
            Instrument3 = musicianProfile("Drum kit", 0, "None")
            print("\tVALID Instrument: ", Instrument3.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test D: Create instrument that is too short")
        try:
            Instrument4 = musicianProfile("An", 0, "None")
            print("\tVALID Instrument: ", Instrument4.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nInstrument Test E: Create instrument that is too long")
        try:
            Instrument5 = musicianProfile("A really long instrument", 0, "None")
            print("\tVALID Instrument: ", Instrument5.music_instrument)
        except Exception as err:
            print("\tERROR: ", err)

    def test_experience(self):
        pass

    def test_group_status(self):
        print("\nGroup Test A: Valid group status")
        try:
            Group1 = musicianProfile("None", 0, "None")
            print("\tVALID Group: ", Group1.group_status)
        except Exception as err:
            print("\tERROR: ", err)

        print("\nGroup Test B: Non-integer group status")
        try:
            Group2 = musicianProfile("None", a, "None")
            print("\tVALID Group: ", Group2.group_status)
        except Exception as err:
            print("\tERROR: ", err)
        print("\nGroup Test C: Integer out of range group status")
        try:
            Group3 = musicianProfile("None", 12, "None")
            print("\tVALID Group: ", Group3.group_status)
        except Exception as err:
            print("\tERROR: ", err)
