class Student:
    def __init__(self, id, name, email, birthdate, address, identifier = ''):
        self._id = id
        self._name = name
        self._email = email
        self._birthdate = birthdate
        self._address = address
        self._identifier = identifier

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
        
    @property
    def birthdate(self):
        return self._birthdate
            
    @property
    def address(self):
        return self._address
    
    @property
    def identifier(self):
        return self._identifier
    
    @property
    def id(self):
        return self._id