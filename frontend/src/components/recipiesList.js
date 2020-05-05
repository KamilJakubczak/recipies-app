import React from 'react';

function RecipiesList(props){
    
  return (
    <React.Fragment>
      {props.recipes.map(recipe => {
        return <h3 key={recipe}>{recipe}</h3>
      })}
    </React.Fragment>
    
  );
}

export default RecipiesList;