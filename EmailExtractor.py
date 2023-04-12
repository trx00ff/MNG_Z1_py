#Zadanie 1 - MNGKW - Regex - Karolina Janiak - WCY19KA1S0
# import re
# class EmailExtractor:
#         email = input("Podaj swój email:")
#        # def __init__(self):
#         pattern = r'^(\w+)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
#         domain = email.split('@')[1]
#
#         match = re.match(pattern, email)
#
#
#         if match:
#                 name = match.group(1)
#                 surname = match.group(2)
#                 status = match.group(3)
#                 domain = 'student'
#                 print("Name:", name)
#                 print("Surname:", surname)
#                 print("Status:", status)
#                 print("Domain:", domain)
#
#
import re

class EmailExtractor:
    def __init__(self, email):
        self.email = email
        self.status = self.is_student()
        self.name = self.get_name()
        self.surname = self.get_surname()
        self.sex = self.is_male()

    def is_student(self):
        pattern = r'^(\w+)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
        pattern = r".+@student.wat.edu.pl"
        return bool(re.match(pattern, self.email))

    def get_name(self):
        pattern = r'^(\w+)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
        match = re.match(pattern, email)
        if match:
                name = match.group(1)
                return name.capitalize() in self.name
        else:
                return "Have you got name? Try again"


    def is_male(self):
        pattern = r'^(a$)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
        match = re.match(pattern, email)
        if match:
                name = match.group(1)
                return "Female" in self.sex
        else:
                return "Male" in self.sex



    def get_surname(self):
        pattern = r'^(\w+)\.(\w+)@(\w+)\.(\w+\.\w+\.\w+)$'
        match = re.match(pattern, email)
        if match:
                surname = match.group(2)
                return surname.capitalize() in self.surname
        else:

        #surname = re.sub(pattern, "", self.email)


email = input("Podaj email:")
ext = EmailExtractor(email)
print("Name:", ext.name)
print("Surname", ext.surname)
print("Status:", ext.status)
print("Sex:", ext.sex)