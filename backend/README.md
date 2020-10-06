# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...
---------------------------------------------------------------------------------------------------------------------------------
//////////////////////////////////////////////////////**The Endpoints**\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
--------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------Get the current categories-------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------
GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
- Example:curl http://localhost:5000/categories
 "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
} 

-----------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------Create new category-------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------
POST '/categories'
- Creates a new  category using the submitted type returns success value and the created category Id.
- the requests body must include json object including the category type.
- Returns:created_category_id (int),success_value(boolean)
- Example:curl -H "Content-type: application/json" -X POST -d '{"type":"math"}' http://localhost:5000/categories

  {
  "created": 8,
  "success": true
}

 -----------------------------------------------------------------------------------------------------------------------------------
 -----------------------------------------Get the current categories and paginated questions ---------------------------------------
 -----------------------------------------------------------------------------------------------------------------------------------
GET '/questions'
- Fetches a list of questions and categories ,current_category and total number of questions
  the list of questions are paginated in groups of 10 
- Request Arguments: page number(optinal)the default value 1
- Returns: a dictionary of  categories, that contains a object of id: category_string key:value pairs. 
           a dictionary of questions,that contains a object of(id(integer),category(integer),answer(text),question(text),rating(integer)).
           a current category (int)
           total number of questions(int)        

  Example:curl http://localhost:5000/questions
 "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": 0,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "rating": 3
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "rating": 4
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 1
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "rating": 3
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 2
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 1
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 3
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "rating": 5
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "rating": 1
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "rating": 2
    }
  ],
  "success": true,
  "total_questions": 20
  }
  -----------------------------------------------------------------------------------------------------------------------------------
  --------------------------------------------------Delete a Question-------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------------
DELETE '/questions/{questionId}'
- Deletes the question of the given ID if it exists returns the ID of the deleted question and success value
- Request Arguments: None
- Returns:deleted_question_id (int),success_value(boolean)
- Example:curl -X DELETE http://localhost:5000/questions/24
{
  "deleted": 24,
  "success": true
}
  -----------------------------------------------------------------------------------------------------------------------------------
  --------------------------------------------------Create new question-------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------------
  POST '/questions'
- Creates a new  question using the submitted question,answer,category,difficulty and rating and returns success value and the created question Id.
- the requests body must include json object including the question attributes.
- Returns:created_question_id (int),success_value(boolean)
- Example:curl -H "Content-type: application/json" -X POST -d '{"question":"What many liters in a gallon?","answer":"3.78","category":1,"difficulty":1,"rating":2}' http://localhost:5000/questions

  {
  "created": 26,
  "success": true
}
 -----------------------------------------------------------------------------------------------------------------------------------
 --------------------------------------------------Get a question based on category-------------------------------------------------------------
 -----------------------------------------------------------------------------------------------------------------------------------
  
 POST '/questions'
- Gets questions based on  category using the submitted category returns dictionary of questions, success value ,total_questions and current_category.
- the requests body must include json object including the category.
- Returns: a dictionary of questions,that contains a object of(id(integer),category(integer),answer(text),question(text),rating(integer)).
           a current category (int)
           total number of questions(int)
           success value (boolean)
- Example: curl -H "Content-type: application/json" -X POST -d '{"current_category":3}' http://localhost:5000/questions
{
  "current_category": 3,
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "rating": 1
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "rating": 2
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 3
}

-----------------------------------------------------------------------------------------------------------------------------------
 --------------------------------------------------Get questions based on search tem-------------------------------------------------------------
 -----------------------------------------------------------------------------------------------------------------------------------
  
 POST '/questions'
- Gets questions based on a search term using the submitted search term returns any questions for whom the search term is a substring of the question, success value ,total_questions and current_category.
- the requests body must include json object including search term.
- Returns: a dictionary of questions,that contains a object of(id(integer),category(integer),answer(text),question(text),rating(integer)).
           a current category (int)
           total number of questions(int)
           success value (boolean)
- Example: curl -H "Content-type: application/json" -X POST -d '{"search":"how"}' http://localhost:5000/questions

 {
  "current_category": 0,
  "questions": [
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 1
}


  -----------------------------------------------------------------------------------------------------------------------------------
  --------------------------------------------------Get next question to play the quiz-------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------------
 
  POST '/questions'
- get a next question to play the quiz.based on submitted category and previous question parameters and return a random question within the given category, if provided, and that is not one of the previous question and the success value.
- the requests body must include json object including the quiz category and previous questions.
- Returns: a question object ,that contains a object of(id(integer),category(integer),answer(text),question(text),rating(integer)).
           success value (boolean)
- Example:  curl -H "Content-type: application/json" -X POST -d '{"quiz_category":2,"previous_questions":[16,17]}' http://localhost:5000/questions
{
  "next_question": {
    "answer": "Jackson Pollock",
    "category": 2,
    "difficulty": 2,
    "id": 19,
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
    "rating": 4
  },
  "success": true
}
  -----------------------------------------------------------------------------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------------
  Error Handling
  ----------------
  Errors are returned as a JSON object in the following format:
  {
     "success":False,
     "error":400,
     "message":"bad request"
  }
  The API will return five error types when the requests fail.
  400 : bad request
  404 : resource not found
  405 : method not allowed
  422 : unprocessable
  500 : internal service error
  ----------------------------------------------------------------------------------------------------------------------------------
  ----------------------------------------------------------------------------------------------------------------------------------

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```