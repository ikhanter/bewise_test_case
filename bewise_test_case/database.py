import os
from dotenv import load_dotenv
from psycopg2 import pool


class DatabaseConnection:

    def __init__(self):
        self.minconn = 0
        self.maxconn = 10
        load_dotenv()
        db_url = os.getenv('DATABASE_URL')
        self.connector = pool.SimpleConnectionPool(self.minconn, self.maxconn, dsn=db_url)  # noqa: E501

    def getconn(self):
        self.conn = self.connector.getconn()

    def putconn(self):
        self.connector.putconn(self.conn)

    def cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def execute(self, *query_content, insert=False):
        self.getconn()
        cursor = self.cursor()
        cursor.execute(*query_content)
        if insert:
            self.conn.commit()
            result = None
        else:
            result = cursor.fetchall()
        cursor.close()
        self.putconn()
        return result
