from flask import Blueprint, render_template, request, redirect, url_for

question = Blueprint('question', __name__)

# Sample questions
quizzes = []



@question.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for quiz in quizzes:
            for i, question in enumerate(quiz['questions']):
                selected = request.form.get(f'question-{i}')
                if selected == question['answer']:
                    score += 1
        return redirect(url_for('question.result', score=score))
    return render_template('quiz.html', quizzes=quizzes, enumerate=enumerate)

@question.route('/result')
def result():
    score = request.args.get('score', type=int)
    return render_template('result.html', score=score, total=len(quizzes))

@question.route('/create-quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        new_question = request.form.get('question')
        new_choices = [request.form.get(f'choice-{i}') for i in range(4)]
        new_answer = request.form.get('answer')
        quizzes.append({"question": new_question, "choices": new_choices, "answer": new_answer})
        return redirect(url_for('question.quiz'))
    return render_template('create-quiz.html')

