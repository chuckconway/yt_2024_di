from databases.database import Database


class SQLServerDatabase(Database):
    def __init__(self, connection_string: str):
        super().__init__(connection_string)
        self.connection_string = connection_string

    def get_user(self, username:str, password: str) -> int | None:
        print(f"Database connection string: {self.connection_string}")
        print(f"Username: {username}")
        print(f"Password: {password}")

        return -1