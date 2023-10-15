from flask import (
    abort,
    Flask,
    jsonify,
    request,
)
from bewise_test_case.service import QuestionService
from bewise_test_case.repository import QuestionRepository
from bewise_test_case.database import DatabaseConnection


db_connector = DatabaseConnection()
question_repo = QuestionRepository(db_connector)
app = Flask(__name__)
question_service = QuestionService(question_repo)


@app.route('/', methods=['GET', 'POST'])
def index():
    questions_num = request.args.get('questions_num')
    if request.method == 'POST':
        if not request.json or 'questions_num' not in request.json:
            abort(400)
        questions_num = request.json['questions_num']
    result = jsonify(question_service.process_questions(questions_num))
    return result
