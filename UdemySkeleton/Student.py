from Login import Login

class Student(Login):
    def __init__(self, name, email):
        super().__init__(name)
        self.__email = email

    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email

    def __str__(self):
        return f"Student: {self.getUsername()}, ID: {self.getId()}, Email: {self.__email}"
    
    