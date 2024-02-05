class Registration:
    def __init__(self, student_id, registration = []):
        self._student_id = student_id
        self._registration = registration

    @property
    def student_id(self):
        return self._student_id
    
    @property
    def registration(self):
        return self._registration