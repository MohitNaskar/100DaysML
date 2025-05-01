class Login:
    id_increamenter = 0 #this will increament the id of the user to make it unique
    def __init__(self,name):
        Login.id_increamenter += 1
        self.__username = name
        self._id = Login.id_increamenter

    def getUsername(self):
        return self.__username
    
    def setUsername(self, name):
        self.__username = name

    def getId(self):
        return self._id
    
    def __str__(self):
        return f"User: {self.__username}, ID: {self._id}"