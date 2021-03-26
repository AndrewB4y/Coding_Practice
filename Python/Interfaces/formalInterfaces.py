"""
Script meant to practice with Python formal interface concept

Resources:
* https://realpython.com/python-interface/

Important notes about Informal Interfaces:

Informal interfaces can be useful for projects with a small code base and
a limited number of programmers. However, informal interfaces would be the
wrong approach for larger applications.
"""

""" Using Abstract method
An abstract method is a method that’s declared by the Python interface,
but it may not have a useful implementation. The abstract method must
be overridden by the concrete class that implements the interface in question.
"""

import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'load_data_source') and
            callable(subclass.load_data_source) and
            hasattr(subclass, 'extract_text') and
            callable(subclass.extract_text)
        )

class PdfParserNew:
    """ Extract text from PDF."""
    
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not overrides FormalParserInterface.extract_text()
        """    
        pass


print("Creating instance of PdfParser")
pdf_parser = PdfParserNew()
print("Creating instance of EmlParser")
eml_parser = EmlParserNew()

print("Checking if the new classes are subclasses")
print(issubclass(PdfParserNew, FormalParserInterface))  # True
print(issubclass(EmlParserNew, FormalParserInterface))  # False


# Using Abstract Method Declaration

"""
An abstract method is a method that’s declared by the Python interface,
but it may not have a useful implementation. The abstract method must be
overridden by the concrete class that implements the interface in question.

To create abstract methods in Python, you add the @abc.abstractmethod
decorator to the interface’s methods. In the next example, you update
the FormalParserInterface to include the abstract methods .load_data_source()
and .extract_text()
"""

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'load_data_source') and
            callable(subclass.load_data_source) and
            hasattr(subclass, 'extract_text') and
            callable(subclass.extract_text) or
            NotImplemented
        )
    
    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError
    
class PdfParserNew(FormalParserInterface):
    """Extract text from PDF."""

    def load_data_source(self, path_str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

print("Creating instance of PdfParserNew")
pdf_parser = PdfParserNew()
print("Creating instance of EmlParserNew")
eml_parser = EmlParserNew()
