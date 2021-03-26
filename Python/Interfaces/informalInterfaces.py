
"""
Script meant to practice with Python informal interface concept

Resources:
* https://realpython.com/python-interface/

Informal Interfaces:

An informal Python interface is a class that defines methods that
can be overridden, but there’s no strict enforcement.

Notes:

Informal interfaces can be useful for projects with a small code base and
a limited number of programmers. However, informal interfaces would be the
wrong approach for larger applications.
"""

class InformalParserInterface:
    """
    Informal interface that defines the methods that will be in both
    the PdfParser and EmlParser concrete classes
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """ Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """ Extract text from the current loading file."""
        pass

"""
To use your interface, you must create a concrete class.
A concrete class is a subclass of the interface that provides
an implementation of the interface’s methods.
"""

class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass

"""
The second concrete class is EmlParser, which you’ll use to
parse the text from emails
"""

class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass

# Check if both PdfParser and EmlParser implement InformalParserInterface
print("Checking if the classes are subclasses")
print(issubclass(PdfParser, InformalParserInterface))  # True
print(issubclass(EmlParser, InformalParserInterface))  # True

# This would return True, which poses a bit of a problem since
# it violates the definition of an interface!

# Now check the method resolution order (MRO) of PdfParser and EmlParser.
# This tells you the superclasses of the class in question, as well as the
# order in which they’re searched for executing a method.

print(PdfParser.__mro__)
print(EmlParser.__mro__)


"""
Ideally, you would want issubclass(EmlParser, InformalParserInterface)
to return False when the implementing class doesn’t define all of the
interface’s abstract methods.

To do this, you’ll create a metaclass called ParserMeta.
You’ll be overriding two dunder methods:
1 .__instancecheck__()
2 .__subclasscheck__()

"""

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass

# Now that ParserMeta and UpdatedInformalParserInterface have been created,
# you can create your concrete implementations.

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass

print("Checking if the new classes are subclasses")
print(issubclass(PdfParserNew, UpdatedInformalParserInterface))  # True
print(issubclass(EmlParserNew, UpdatedInformalParserInterface))  # False


