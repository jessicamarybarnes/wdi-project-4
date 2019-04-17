import React from 'react'
import Select from 'react-select'
import { withRouter } from 'react-router-dom'

import axios from 'axios'
// import { colourOptions } from '../data'
// import { Note } from '../styled-components'

class Search extends React.Component {
  constructor() {
    super()

    this.state = {
      selectedOption: null,
      meals: []
    }

    this.handleChange = this.handleChange.bind(this)
    this.getMeals = this.getMeals.bind(this)
  }

  componentDidMount() {
    console.log(this.state.options)
    this.getMeals()
  }

  getMeals() {
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


  handleChange(selectedOption) {
    console.log('changed', selectedOption)
    this.setState({ selectedOption })
    this.props.history.push(`/meals/${selectedOption.value}`)
    console.log('selected Options is: ', selectedOption.value)
  }

  render() {
    const { selectedOption } = this.state
    return (
      <div>
        <Select
          className="basic-single"
          classNamePrefix="select"
          value={selectedOption}
          onChange={this.handleChange}
          options={this.state.meals.map(meal => ({
            value: meal.id,
            label: meal.meal_name
          }))}
        />
      </div>
    )
  }
}

export default withRouter(Search)
