class TooManyStudentsError(Exception):
    def __init__(self, message="The group cannot contain more than 10 students"):
        self.message = message
        super().__init__(self.message)
