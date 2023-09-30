from flask import Flask, render_template, request

app = Flask(__name__)


python_questions = [
    {
        'question': 'What is the result of 2 + 2?',
        'options': ['3', '4', '5', '6'],
        'correct_answer': '4'
    },
    {
        'question': 'Which keyword is used to define a function in Python?',
        'options': ['def', 'function', 'define', 'func'],
        'correct_answer': 'def'
    },
    {
        'question': 'In Python, which data structure is used to store an ordered collection of items?',
        'options': ['List', 'Tuple', 'Dictionary', 'Set'],
        'correct_answer': 'List'
    },
    {
        'question': "What is the purpose of the 'elif' statement in Python?",
        'options': ['It is used to define a function.', 'It is used to handle exceptions.', 'It is used to create a loop.', 'It is used to add additional conditions to an "if" statement.'],
        'correct_answer': 'It is used to add additional conditions to an "if" statement.'
    },
]


web_dev_questions = [
    {
        'question': 'What does HTML stand for?',
        'options': ['Hyper Text Markup Language', 'Highly Typed Markdown Language', 'Hyper Transfer Markup Language', 'Hyperlink and Text Markup Language'],
        'correct_answer': 'Hyper Text Markup Language'
    },
    {
        'question': 'Which programming language is used for front-end web development?',
        'options': ['Python', 'Java', 'JavaScript', 'C++'],
        'correct_answer': 'JavaScript'
    },
    {
        'question': 'Which HTML tag is used to create a hyperlink?',
        'options': ['<link>', '<a>', '<href>', '<url>'],
        'correct_answer': '<a>'
    },
    {
        'question': 'What is the purpose of CSS (Cascading Style Sheets) in web development?',
        'options': ['To define the structure and content of a web page.', 'To handle server-side scripting.',
                    'To specify the layout and design of a web page.', 'To store data on the web server.'],
        'correct_answer': 'To specify the layout and design of a web page.'
    },
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/python-quiz')
def show_python_quiz():
    return render_template('python-quiz.html', questions=python_questions, quiz_type='python')


@app.route('/web-dev-quiz')
def show_web_dev_quiz():
    return render_template('web-dev-quiz.html', questions=web_dev_questions, quiz_type='web_dev')


@app.route('/quiz/<quiz_type>', methods=['POST'])
def quiz(quiz_type):
    print(f"Received quiz_type: {quiz_type}")

    if quiz_type == 'python':
        questions = python_questions
    elif quiz_type == 'web-dev':
        questions = web_dev_questions
    else:
        return "Invalid quiz type"

    score = calculate_score(questions)
    return render_template('quiz.html', score=score, total=len(questions), quiz_type=quiz_type)


def calculate_score(questions):
    score = 0
    for question in questions:
        user_answer = request.form.get(question['question'])
        if user_answer == question['correct_answer']:
            score += 1
    return score


if __name__ == '__main__':
    app.run(debug=True)
