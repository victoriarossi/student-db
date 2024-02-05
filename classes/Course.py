class Course:
    def __init__(self, code, name, credits, prerequisites, description = ""):
        self._code = code
        self._name = name
        self._credits = credits
        self._prerequisites = prerequisites
        self._description = description

    @property
    def code(self):
        return self._code
    
    @property
    def name(self):
        return self._name
    
    @property
    def credits(self):
        return self._credits
    
    @property
    def description(self):
        return self._description
    
    @property
    def prerequisites(self):
        return self._prerequisites