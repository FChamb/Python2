# TODO: Add DataSet class that others can implement

import enum
from enum import Enum

class DataSet:
    """Represents a particular dataset that can be analysed

    This class provides the `path` of the data file (relative to data/)
    as well as a mapping from column names to column specifications.
    """
    def __init__(self, path, colMap):
        self.path = path
        self.colMap = colMap

    def get_column(self, colName):
        """Get the Column specification by column name

        This returns a Column object, which defines the expected
        data values and mappings for a particular column in
        the data set.
        """
        return self.colMap[colName]

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
    """Abstraction to represent different possible values and their encodings

    == Implementing ==
    To use, extend and create options as `class member = (key, desc)`
    This will then provide class members that can be used like enums.

    == Iteration ==
    You can iterate over the class members using normal iteration
    syntax: [x for x in SubClass]. These give you the class members
    which you can then call

    == Mappings ==
    If you have a key and want to map to the enum, you can use parse()
    You can then do .key() or .desc() to obtain its key and description

    For when more performant code is required, a `mapping` dictionary is created
    on this class. The mapping dictionary maps directly from key to description.
    You can use this directly, such as with pandas dataframes .replace to
    achieve much higher performance when needed.
    """

    # https://stackoverflow.com/questions/56735081/add-and-initilalize-an-enum-class-variable-in-python
    def __init__(self, k, v):
        # Intiialise a class member variable mapping with all enums in
        super().__init__()
        if self.__class__.__dict__.get('mappings', None) is None:
            self.__class__.mappings = {}
        self.__class__.mappings[k] = v

    @classmethod
    def parse(cls, encoded):
        """Parses the encoded key into a enum variant"""
        for member in cls:
            if member.key() == encoded:
                return member
        raise KeyError("No member with key: " + encoded)

    @classmethod
    def keys(cls):
        """Returns a list of the valid keys for this option"""
        return [m.key() for m in cls]

    def key(self):
        """Gets the key, i.e. the encoded value for this option"""
        return self.value[0]

    def desc(self):
        """Gets the human readable description of what this option means"""
        return self.value[1]

    def __str__(self):
        """Returns a human readable description of what this enum signified"""
        return self.desc()

    def __repr__(self):
        """Returns a representation of this enum with both value and type information"""
        return f"<{self.__class__.__name__}: {self.key()} -> {self.name}>"
