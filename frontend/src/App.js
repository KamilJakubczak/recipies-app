import React, {Component} from 'react';
import './App.css';

import RecipiesList from './components/recipiesList';

class App extends Component {

  recipes = ['scrabled eggs','sousage']; 
  componentDidMount(){
    // Fetch data when the component is mount
    fetch('http://127.0.0.1:8000/api/meal/',{
      method: 'GET',
    }).then(resp => console.log(resp))
    .catch(error => console.log(error))
  }
  
  render(){
    return (
      <div className="App">
        <header className="App-header">
          <h1>Recipes</h1>
          <RecipiesList recipes={this.recipes} />
        </header>
      </div>
    );
  }
  
}

export default App;
