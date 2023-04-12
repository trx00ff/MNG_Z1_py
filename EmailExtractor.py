#Zadanie 1 - MNGKW - Regex - Karolina Janiak - WCY19KA1S0

import re

class EmailExtractor:


    def __init__(self, email):
        self.email = email
        self.status = self.is_student()
        self.name = self.get_name()
        self.surname = self.get_surname()
        self.gender = self.is_male()

    def is_student(self):
        pattern = r'(\w+)\.(\w+)@student.wat.edu.pl'
        return bool(re.match(pattern, self.email))

    def get_name(self):
        pattern = r'^(\w+)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
        match = re.match(pattern, email)
        if match:
                name = match.group(1)
                return name.capitalize()
        else:
                return ValueError('Have you got name? Try again')


    def is_male(self):
        pattern = r'^(a$)\.(\w+)@(\w+)\.wat.edu.pl'
        match = re.match(pattern, email)
        if match:
                name = match.group(1)
                print('female')
        else:
                print('male')



    def get_surname(self):
        pattern = r'^(\w+)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
        match = re.match(pattern, email)
        if match:
                surname = match.group(2)
                return surname.capitalize()
        else:
                return ValueError('Have you got surname? Try again')
        #surname = re.sub(pattern, '', self.email)


email = input('Podaj email:')
ext = EmailExtractor(email)
print('Name:', ext.name)
print('Surname', ext.surname)
print('Student:', ext.status)
print('Gender:', ext.gender)