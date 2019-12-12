class Skill(object):
    """Represents a sporting skill and the level attained."""

    def __init__(self, skill_name, level):
        """
        Constructor for the Skill class.

        :param str skill_name: Name of the sports skill.
        :param int level: int Level attained, integer values 1 to 10.
        """
        self._skill_name = skill_name
        self._level = level

    def __str__(self):
        return "Skill: {}, Level: {}.".format(self._skill_name, self._level)

    def __repr__(self):
        return "Skill: {}, Level: {}.".format(self._skill_name, self._level)


class User(object):
    """Represents a user for authentication purposes."""

    def __init__(self, username, password):
        """
        Constructor for the User class.

        :param str username: Username must be unique.
        :param str password: Password.
        """
        self.username = username
        self.password = password


class Athlete(User):
    """Represents an athlete."""

    def __init__(self, first_name, last_name, dob, username, password):
        """
        Constructor for the Athlete class.

        :param str first_name: First name.
        :param str last_name: Family name or surname.
        :param str dob: Date of birth.
        """
        super().__init__(username, password)
        self.first_name = first_name  # instance variable
        self.last_name = last_name
        self.dob = dob
        self.club = None
        self.skills = []

    def __str__(self):
        return "Fullname: {} Club: {} Skills: {}".format(self.fullname, self.club, self.skills)

    def add_skill(self, skill_name):
        """
        Adds a skill object to the skills attribute list. Checks that the object is of type skill.

        :param Skill skill_name: Name of the skill
        :rtype: None
        :raises TypeError: If skill_name is not of object type Skill
        """
        if not isinstance(skill_name, Skill):
            raise TypeError("Skill object doesn't have type \"Skill\".")
        self.skills.append(skill_name)

    @property
    def fullname(self):
        """Defines the full name attribute using the first and last name attributes"""
        return self.first_name + ' ' + self.last_name

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None


# You do not need the following in your class for the coursework,
# it is included so you can see output from docstrings and __str__.
if __name__ == "__main__":
    help(Athlete)
    a1 = Athlete("Jo", "Bloggs", "31/12/1999", "jobl3214", "password_hash")
    print(str(a1))
    a1.club = "ABC running club"
    print(str(a1))
    sk1 = Skill("Sprint", 5)
    sk2 = Skill("Javelin", 3)
    a1.add_skill(sk1)
    a1.add_skill(sk2)
    print(str(a1))
