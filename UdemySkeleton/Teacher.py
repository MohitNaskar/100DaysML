from Login import Login

class Teacher(Login):
    def __init__(self, name, subject):
        super().__init__(name)
        self.__subject = subject

    def getSubject(self):
        return self.__subject
    
    def setSubject(self, subject):
        self.__subject = subject

    def __str__(self):
        return f"Teacher: {self.getUsername()}, ID: {self.getId()}, Subject: {self.__subject}"