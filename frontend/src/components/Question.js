import React, { Component } from 'react';
import '../stylesheets/Question.css';

class Question extends Component {
  constructor(){
    super();
    this.state = {
      visibleAnswer: false
    }
  }

  flipVisibility() {
    this.setState({visibleAnswer: !this.state.visibleAnswer});
  }
    getImage = (category) => {
        var builtInCategories = ['Geography', 'History', 'Sports', 'Science', 'Art', 'Entertainment'];
        if (builtInCategories.includes(category )) 
            return `${category}.svg`;
        
       
        return 'general.svg';    
    }

  render() {
    const { question, answer, category, difficulty,rating } = this.props;
    return (
      <div className="Question-holder">
        <div className="Question">{question}</div>
        <div className="Question-status">
                <img className="category" src={this.getImage(category)} />
                <div className="difficulty">Difficulty: {difficulty}</div>
                <div className="rating">Rating: {rating}</div>


          <img src="delete.png" className="delete" onClick={() => this.props.questionAction('DELETE')}/>    
        </div>
        <div className="show-answer button"
            onClick={() => this.flipVisibility()}>
            {this.state.visibleAnswer ? 'Hide' : 'Show'} Answer
          </div>
        <div className="answer-holder">
          <span style={{"visibility": this.state.visibleAnswer ? 'visible' : 'hidden'}}>Answer: {answer}</span>
        </div>
      </div>
    );
  }
}

export default Question;
