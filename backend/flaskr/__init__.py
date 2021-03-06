import os
from flask import Flask, request, abort, jsonify
from sqlalchemy.sql.expression import func
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS,cross_origin
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request,selection):
    page =request.args.get('page',1,type=int)
    start = (page-1)*QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions =questions[start:end]
    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods','GET,POST,PATCH,DELETE,OPTIONS')
      response.headers.add('Access-Control-Allow-Origin','*')
      return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def retrieve_categories():
      results = Category.query.order_by(Category.id).all()
      categories = {category.id:category.type for category in results}
     
      if len(categories)==0:
          abort(404)

      return jsonify({
            'success':True,
            'categories':categories})


  @app.route('/categories',methods =['POST'])
  def create_category():
      body = request.get_json()
      if body is None:
          abort (400)
      if 'type' not in body:
          abort(400)
      new_type =body.get('type',None)

      try:
          
          category = Category(type=new_type)
          category.insert()
         
          return jsonify({
                'success':True,
                'created':category.id})
      except:
          abort(422)

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
 
  @app.route('/questions')
  def retrieve_questions():
      current_questions=None
      categories=None
      selection = Question.query.order_by(Question.id).all()
      if len(selection)> 0:
          current_questions = paginate_questions(request,selection)
      results = Category.query.order_by(Category.id).all()
      if len(results) > 0:
          categories = {category.id:category.type for category in results}
      return jsonify({
            'success':True,
            'questions':current_questions,
            'total_questions':len(selection),
            'categories':categories,
            'current_category': 0
            })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>',methods=['DELETE'])
  def delete_question(question_id):
      question = Question.query.filter(Question.id==question_id).one_or_none() 
      if question is None:
          abort(404)
      try:
          question.delete()
          #selection = Question.query.order_by(Question.id).all()  
          #current_questions = paginate_questions(request,selection)
          return jsonify({
            'success':True,
            'deleted':question_id
            #,'questions':current_questions,
            #'total_questions':len(selection)
            })
      except :
          abort(422)
         

     
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions',methods =['POST'])
  def create_question():
      
      body = request.get_json()
      if not body:
          abort(500)
      new_question =body.get('question',None)
      new_answer =body.get('answer',None)
      new_category =body.get('category',None)
      new_difficulty = body.get('difficulty',None)
      new_rating = body.get('rating',None)
      search = body.get('search',None)
      current_category=body.get('current_category',None)
      previous_questions = body.get('previous_questions',None)
      quiz_category = body.get('quiz_category',None)
      if search:
          selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search))).all()
          if len(selection)==0:
              abort(404)
          current_questions = paginate_questions(request,selection)
          return jsonify({
            'success':True,
            'questions':current_questions,
            'total_questions':len(selection),
            'current_category':0})
      elif current_category:
          
          if current_category != 0:
              selection=Question.query.order_by(Question.id).filter(Question.category==current_category).all()
          else:
              selection=Question.query.order_by(Question.id).all()
          if len(selection)==0:
              abort(404)
          current_questions = paginate_questions(request,selection)
          
          return jsonify({
                    'success':True,
                     'questions':current_questions,
                     'total_questions':len(selection),
                     'current_category':current_category})
      elif quiz_category:
          if previous_questions:
              result=Question.query.order_by(func.random()).filter(Question.category==quiz_category).filter(~ Question.id.in_(previous_questions)).first()
          else:
              result=Question.query.order_by(func.random()).filter(Question.category==quiz_category).first()
          if not result:
              question = None
          else:
              question = result.format()
         
          return jsonify({
            'success':True,
            'next_question':question})
      elif new_question:
          try:
              question = Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty,rating=new_rating)
              question.insert()
             
              return jsonify({
                'success':True,
                'created':question.id
                })
          except:
              abort(422)
      else:
          abort(400)

      

 

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  
  

     

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  
  

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
           'success':False,
            'error':404,
            'message':'resource not found' }),404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
           'success':False,
            'error':422,
            'message':'unprocessable' }),422

  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
           'success':False,
            'error':405,
            'message':'method not allowed' }),405

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
           'success':False,
            'error':400,
            'message':'bad request' }),400

  @app.errorhandler(500)
  def internal_service_error(error):
      return jsonify({
           'success':False,
            'error':500,
            'message':'internal service error' }),500
  return app

    