from .database.mysql import MySQLDatabase
from .database.postgres import PostgresDatabase
from .interfaces import Connection, Database


def connect_and_print_result(database: Database) -> None:
    connection: Connection = database.connect("url_de_example")
    result = connection.execute("query de exemplo")
    for element in result:
        print(element)


def main() -> None:
    database_name = input("Database: ").lower()

    if database_name == "postgres":
        connect_and_print_result(PostgresDatabase())
    elif database_name == "Myql":
        connect_and_print_result(MySQLDatabase())
    else:
        raise ValueError("Database invalid!")

    if __name__ == "__main__":
        main()
