from databases.database import Database
from databases.postgres_database import PostgresDatabase


class User:
    def __init__(self, first_name: str, last_name: str, database: Database):
        self.database = database
        self.first_name = first_name
        self.last_name = last_name

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def is_authenticated(self, username: str, password: str) -> bool:
        user_id = self.database.get_user(username, password)
        return user_id > 0