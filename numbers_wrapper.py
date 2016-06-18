import numbers


class NaturalNumber(numbers.Number):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, NaturalNumber):
            return self.value == other.value
        if isinstance(other, numbers.Real):
            return self.value == other
        return NotImplemented


class RealNumber(NaturalNumber):
    def __init__(self, value):
        super(RealNumber, self).__init__(value)
