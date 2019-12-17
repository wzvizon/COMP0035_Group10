# Weizheng Zhang
# ID: 16081188
#THIS IS A VENUE PROFILE CLASS

class VenueProfile:

    MAX_LENGTH = 50
    MAX_TYPE_RANGE = 6
    MIN_TYPE_RANGE = 0

    def __init__(self, venue_name, venue_capacity, venue_type):
        self.v_name = venue_name
        self.v_capacity = venue_capacity
        self.v_type = venue_type

    def __str__(self):
        if self.v_type == 1:
            the_type = "academic venue"
        elif self.v_type == 2:
            the_type = "club"
        elif self.v_type == 3:
            the_type = "restaurant"
        elif self.v_type == 4:
            the_type = "cruise"
        elif self.v_type == 5:
            the_type = "concert hall"
        else:
            the_type = "other types"
        return "\nVenue's name: {} \nCapacity: {} \nType: {}" \
                .format(self.v_name, self.v_capacity, the_type)

    @property
    def v_name(self):
        return self._venue_name

    @v_name.setter
    def v_name(self, venue_name):
        self.validate_length(venue_name)
        self._venue_name = venue_name

    @property
    def v_capacity(self):
        return self._venue_capacity

    @v_capacity.setter
    def v_capacity(self, venue_capacity):
        self.validate_format(venue_capacity)
        self._venue_capacity = venue_capacity

    @property
    def v_type(self):
        return self._venue_type

    @v_type.setter
    def v_type(self, venue_type):
        self.validate_range(venue_type)
        self._venue_type = venue_type

    @staticmethod
    def validate_length(v_name):
        if len(v_name) > VenueProfile.MAX_LENGTH:
            raise TypeError('Invalid venue name: name too long')
        elif len(v_name) == 0:
            raise TypeError('Invalid name: Please input a name')

    @staticmethod
    def validate_format(v_capacity):
        if type(v_capacity) != int:
            raise TypeError('Invalid capacity: please enter a number')
        if v_capacity == 0:
            raise ValueError('Invalid number: please enter a valid number')
        return True

    @staticmethod
    def validate_range(v_type):
        if v_type > VenueProfile.MAX_TYPE_RANGE or v_type < VenueProfile.MIN_TYPE_RANGE:
            raise ValueError('Invalid type: please choose the type between 0 and 6')
        return True

def main():
    try:
        v1 = VenueProfile('Royal Albert Hall', 500, 5)
        print(v1)
    except Exception as err:
        print(err)

    try:
        v2 = VenueProfile('Room 410', 0, 1)
        print(v2)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()