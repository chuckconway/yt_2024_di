import unittest
from unittest.mock import patch

from databases.mock_database import MockDatabase
from databases.postgres_database import PostgresDatabase

from user import User


class UserTest(unittest.TestCase):
    def test_is_authenticated(self):
        database = MockDatabase('connection_string')
        database.get_user = lambda username, password: -1


        is_authenticated = (User('John', 'Doe', database)
                           .is_authenticated('username', 'password'))

        self.assertTrue(is_authenticated)

    @patch.object(PostgresDatabase, 'get_user')
    def test_is_authenticated_patched(self, mock_is_authenticated):
        mock_is_authenticated.return_value = -1

        is_authenticated = (User('John', 'Doe')
                            .is_authenticated('username', 'password'))

        self.assertTrue(is_authenticated)
