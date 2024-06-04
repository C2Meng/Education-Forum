from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Quiz, Question, Answer, User
from website import db
from flask_login import current_user

question = Blueprint('question', __name__)

@question.route('/my-quiz', methods = ['GET', 'POST'] )
def my_quiz():
    user= User.query.all()
    quizzes = Quiz.query.all()
    return render_template('my-quiz.html', quizzes=quizzes, user=current_user)

@question.route('/create-quiz', methods = ['GET','POST'])
def create_quiz():
   if request.method == 'POST':
        title = request.form['title']
        subject = request.form['subject']
        question_text = request.form['question']
        choices = request.form.getlist('choices')
        correct_answer = request.form['correct_answer']
        
        
        # Create the quiz
        quiz = Quiz(title=title, subject=subject, description=f"Quiz on {subject}")
        db.session.add(quiz)
        db.session.commit()
        
        # Create the question
        question = Question(text=question_text, quiz_id=quiz.id)
        db.session.add(question)
        db.session.commit()
        
        # Create the answers
        for choice in choices:
            is_correct = (choice == correct_answer)
            answer = Answer(text=choice, is_correct=is_correct, question_id=question.id)
            db.session.add(answer)
        
        db.session.commit()
        
        return redirect(url_for('question.display_quiz', quiz_id=quiz.id))
   
   return render_template('create-quiz.html', user=current_user)
   
@question.route('/display-quiz/<int:quiz_id>', methods=['GET', 'POST'])
def display_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
   
    return render_template('quiz.html', quiz=quiz, user=current_user)


@question.route('/submit-quiz/<int:quiz_id>', methods=['POST'])
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    score = 0
    total_questions = len(quiz.questions)
    for question in quiz.questions:
        selected_answer_id = request.form.get(f'question_{question.id}')
        selected_answer = Answer.query.get(selected_answer_id)
        if selected_answer and selected_answer.is_correct:
            score += 1
    
    return render_template('result.html', quiz=quiz, score=score, total_questions=total_questions, user=current_user)

@question.route('/admin_home',methods = ['GET', 'POST'] )
def admin_home():
    quizzes = Quiz.query.all()
    return render_template('admin_home.html', quizzes=quizzes, user=current_user)

