"""The file is going to contain the hashing logic"""
from passlib.context import CryptContext


password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash():
    """The hashing class"""

    def password_hash(self, _password: str):
        """A function meant to hash the password

        Args:
            _password (str): The password

        Returns:
            str: The password hash
        """
        return password_context.hash(_password)
