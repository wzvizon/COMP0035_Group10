# Bryan Gunawan
# SN:17080399

class user_account:

    MAX_LENGTH = 10
    MAX_USERNAME_LENGTH = 10
    MAX_PASSWORD_LENGTH = 10

    def __init__(self, the_firstname, the_surname, the_email, the_username, the_password):
        self.firstname = the_firstname
        self.surname = the_surname
        self.email = the_email
        self.username = the_username

    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, the_firstname):
        self.validate_name_format(the_firstname)
        self._firstname = the_firstname

    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, the_surname):
        self.validate_name_format(the_surname)
        self._surname = the_surname

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, the_email):
        self.validate_address(the_email)
        self._email = the_email

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, the_username):
        self.validate_username_length(the_username)
        self._username = the_username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, the_password):
        self.validate_password_length(the_password)
        self._username = the_password

    def __str__(self):
        return self.username
    
    # Validate format to not contain numbers
    @staticmethod
    def validate_name_format(name):
        if type(name) != str:
            raise TypeError('Invalid name: please enter text')
        if any(char.isdigit() for char in name):
            raise TypeError('Invalid name: please do not use number')
        return True
    
    # Validate email address to find @
    @staticmethod
    def validate_address(email):
        char = []
        address = []
        index = 0
        for ch in range(len(email)):
            if email[ch] != '@':
                index += 1
            char.append(email[ch])

        for i in range(index,len(email)):
            address.append(email[i])
        
        if index == len(email):
            raise TypeError('Invalid email address: @ not found')
        return True

    # Validate username length
    @staticmethod
    def validate_username_length(username):
        if len(username) > user_account.MAX_USERNAME_LENGTH:
            raise TypeError('Invalid username: username too long')
        elif len(username) == 0:
            raise TypeError('Invalid username: Please input username')

    # Validate password length
    @staticmethod
    def validate_password_length(password):
        if len(password) > user_account.MAX_PASSWORD_LENGTH:
            raise TypeError('Invalid password: password too long')
        elif len(password) == 0:
            raise TypeError('Invalid password: Please input password')

def main():
    try:
        email1 = user_account('bryan','gunawan','bryan@ucl.com','bryanadg','password123')
        print(email1)
    except Exception as err:
        print(err)

    try:
        email2 = user_account('bryan','5urn4m3','noaddress','verylongusername','password123')
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
