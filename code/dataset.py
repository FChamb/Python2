# TODO: Add DataSet class that others can implement

from enum import Enum

# class to represent column
class Column:
    """Represents specification of a column in a dataset

    Includes the type of data that should be in the column
    and may also provided a limited set of permitted values
    """
    def __init__(self, options, type):
        self.options = options
        self.values = None if options is None else options.keys()
        self.type = type

class OptionEnum(Enum):
    """Represents possible values allowed in a particular column
    """
    @classmethod
    def parse(cls, encoded):
        """Parses the encoded key into a enum variant"""
        for m in cls:
            if encoded == m.key():
                return m
        raise KeyError(str(encoded) + " is not a valid key for " + str(cls))

    @classmethod
    def keys(cls):
        """Returns a list of the valid keys for this option"""
        return [m.key() for m in cls]

    def key(self):
        return self.value[0]

    def desc(self):
        return self.value[1]

    def __str__(self):
        """Returns a human readable description of what this enum signified"""
        return self.desc()

    def __repr__(self):
        """Returns a representation of this enum with both value and type information"""
        return f"<{self.__class__.__name__}: {self.key()} -> {self.name}>"
