from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .models import Quiz, Question, Answer, User, StudentResult
from website import db
from flask_login import current_user
import json

question = Blueprint('question', __name__)




#displays all quizzes
@question.route('/my_quiz', methods = ['GET', 'POST'] )
def my_quiz():
    user= User.query.all()
    quizzes = Quiz.query.all()
    return render_template('my_quiz.html', quizzes=quizzes, user=current_user)




#creating quiz from scratch
@question.route('/create_quiz', methods = ['GET','POST'])
def create_quiz():
   if request.method == 'POST':
        title = request.form['title']
        subject = request.form['subject']
        question_text = request.form['question']
        choices = request.form.getlist('choices')
        correct_answer = request.form['correct_answer']
        
        
        # Create the quiz
        quiz = Quiz(
            title=title, 
            subject=subject, 
            description=f"Quiz on {subject}",
            user_id=current_user.id
            )
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
        
        return redirect(url_for('question.view_quiz', quiz_id = quiz.id))
        #return redirect(url_for('question.display_quiz', quiz_id=quiz.id))
   
   return render_template('create_quiz.html', user=current_user)




#route to add more question to a specific quiz
@question.route('add_question/<int:quiz_id>', methods=['GET', 'POST'])
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        
        question_text = request.form['question']
        choices = request.form.getlist('choices')
        correct_answer = request.form['correct_answer']

        question = Question(text=question_text, quiz_id=quiz.id)
        db.session.add(question)
        db.session.commit()

        for choice in choices:
            is_correct = (choice == correct_answer)
            answer = Answer(text=choice, is_correct=is_correct, question_id=question.id)
            db.session.add(answer)
        
        db.session.commit()
        return redirect(url_for('teacher.admin_home', quiz_id = quiz.id)) #link to teacher.py and admin_home

    return render_template('add_question.html', user=current_user, quiz=quiz)




#answering quiz   
@question.route('/display_quiz/<int:quiz_id>', methods=['GET', 'POST'])
def display_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
   
    return render_template('quiz.html', quiz=quiz, user=current_user)




#viewing quiz only
@question.route('/view_quiz/<int:quiz_id>', methods=['GET', 'POST'])
def view_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)

    return render_template('view_quiz.html', quiz=quiz, user=current_user)


#deleting a quiz
@question.route('/delete_quiz/<int:quiz_id>', methods=['POST'])
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)

    #making sure authorisation to delete quiz is there
    if quiz.user_id == current_user.id:
            questions = Question.query.filter_by(quiz_id=quiz_id).all()
            for question in questions:
                answers = Answer.query.filter_by(question_id=question.id).all()
                for answer in answers:
                    db.session.delete(answer)
                db.session.delete(question)
            db.session.delete(quiz)
            db.session.commit()

            flash('Quiz deleted successfully.',  category='success')
            return redirect(url_for('teacher.admin_home'))

    else:
        flash('You do not have authorisation to delete this quiz.',  category='error')
        return redirect(url_for('teacher.admin_home'))

    
#add user relevant quiz

#submitting quiz to get result
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

    #store score into db
    student_result = StudentResult(
        quiz_id=quiz.id,
        user_id=current_user.id,
        score=score
    )
    db.session.add(student_result)
    db.session.commit()
    
    return render_template('score.html', quiz=quiz, score=score, total_questions=total_questions, user=current_user)


@question.route('/share_quiz/<int:quiz_id>', methods=['GET', 'POST'])
def share_quiz(quiz_id):
    ori_quiz=Quiz.query.get_or_404(quiz_id)

    #copy quiz
    copy_quiz=Quiz(
        title=ori_quiz.title, 
        subject=ori_quiz.subject, 
        description=f"Quiz on {ori_quiz.subject}",
        user_id=current_user.id
    )
    db.session.add(copy_quiz)
    db.session.commit()

    #copy question
    for ori_question in ori_quiz.questions:
        copy_question=Question(text=ori_question.text, quiz_id=copy_quiz.id)
        db.session.add(copy_question)
        db.session.commit()

        for ori_answer in ori_question.answers:
            copy_answer=Answer(
                text=ori_answer.text, 
                is_correct=ori_answer.is_correct, 
                question_id=copy_question.id)
            db.session.add(copy_answer)

    db.session.commit()

    flash('Quiz shared succesfully!', 'success')
    return redirect(url_for('teacher.admin_home', quiz_id=copy_quiz.id))

    
    

