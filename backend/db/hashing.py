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

    def verify_password(self, plain_password: str, hashed_password: str):
        """A function to verify the passwords after hashing

        Args:
            plain_password (str): The plain password
            hashed_password (str): The passwords after being hashed

        Returns:
            bool: Whether they re teh same on not
        """
        return password_context.verify(plain_password, hashed_password)
