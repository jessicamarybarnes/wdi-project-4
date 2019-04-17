import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

class Suggestion extends React.Component {
  constructor() {
    super()

    this.state = {
      meals: []
    }
  }

  componentDidMount() {
    const meals = []
    axios.get('/api/meals')
      .then(res => res.data.forEach(function(meal){
        const mealNames = []
        meals.forEach(function(savedMeal){
          mealNames.push(savedMeal.meal_name)
        })
        if(!mealNames.includes(meal.meal_name)) {
          meals.push(meal)
          console.log('meals', meals)
        }
      }))
      .then(() => this.setState({ meals: meals }))
  }

  render() {
    return(
      <div className="container suggestions">
        <div className="columns is-multiline">
          {this.state.meals.map(meals =>
            <div key={meals.id} className="column is-one-third">
              <Link to={`meals/${meals.id}`}>
                <div className="meal-image pink" style={{ backgroundImage: `url(${meals.meal_image})` }}>
                  <h1>{meals.meal_name}</h1>
                </div>
              </Link>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default Suggestion
