from bewise_test_case.database import DatabaseConnection
import datetime


class QuestionRepository:
    connector = None

    def __init__(self, connector: DatabaseConnection):
        self.connector = connector

    def add_question(self, question: dict):
        self.connector.execute('''INSERT INTO questions (question_id, question, answer, created_at, added)
                               VALUES (%s, %s, %s, %s, %s);''',  # noqa: E501
                               (question['id'], question['question'], question['answer'], question['created_at'], datetime.datetime.now()),  # noqa: E501
                               insert=True)

    def check_question(self, question_id: int):
        result = self.connector.execute('SELECT * FROM questions WHERE question_id=%s', (question_id,))  # noqa: E501
        return not result

    def get_last_added(self):
        result = self.connector.execute('SELECT * FROM questions ORDER BY added DESC LIMIT 1;')  # noqa: E501
        return result
