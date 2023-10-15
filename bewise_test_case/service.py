from bewise_test_case.repository import QuestionRepository
import requests


class QuestionService:
    repo = None

    def __init__(self, repo: QuestionRepository):
        self.repo = repo

    def __preprocess(self, questions_num) -> dict:
        if not questions_num:
            return None
        data = requests.get('https://jservice.io/api/random', params=[('count', questions_num)])  # noqa: E501
        questions = data.json()
        return questions

    def __format_datetime(self, question: tuple) -> dict:
        labels = ('id', 'question_id', 'question', 'answer', 'created_at', 'added')  # noqa: E501
        result = dict(zip(labels, question))
        result['created_at'] = result['created_at'].strftime("%Y-%m-%d %H:%M:%S")  # noqa: E501
        result['added'] = result['added'].strftime("%Y-%m-%d %H:%M:%S")
        return result

    def process_questions(self, questions_num: int) -> dict:
        last_question = self.repo.get_last_added()
        if not last_question:
            last_question = {}
        else:
            last_question = self.__format_datetime(last_question[0])

        if not questions_num:
            questions_num = 0

        def add_questions(num: int):
            result = self.__preprocess(num)
            counter = 0
            if result:
                for r in result:
                    if self.repo.check_question(r['id']):
                        self.repo.add_question(r)
                    else:
                        counter += 1
            if counter == 0:
                return True
            return add_questions(counter)

        hundred_query_count = questions_num // 100
        last_query_questions_num = questions_num % 100
        for i in range(hundred_query_count):
            add_questions(100)
        add_questions(last_query_questions_num)
        return last_question
