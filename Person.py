class Person:
    lastIdUsed = 100

    def __str__(self):
        return "{} {} {}".format(self._fName, self._lName, self._id)
