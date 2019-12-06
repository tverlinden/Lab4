class Person:
    lastIdUsed = 100

    def __init__(self, fName, lName, id):
        self._fName = fName
        self._lName = lName
        self._id = id

    def __str__(self):
        return "{} {} {}".format(self._fName, self._lName, self._id)
