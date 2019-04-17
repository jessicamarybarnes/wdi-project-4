import React from 'react'
import ReactDOM, { render } from 'react-dom'
import { Link, withRouter } from 'react-router-dom'
import axios from 'axios'
import ReactStars from 'react-stars'


class MealCategory extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      mealsCategory: []
    }

    this.getMealCategory = this.getMealCategory.bind(this)
    this.averageRating = this.averageRating.bind(this)
  }

  componentDidMount() {
    this.getMealCategory()
  }

  componentDidUpdate(prevProps) {
    if (this.props.location.pathname !== prevProps.location.pathname) {
      this.getMealCategory()
    }
  }

  getMealCategory() {
    axios.get('/api/meals')
      .then(res => {
        const mealMatched = res.data.filter(({ id }) => id === parseInt(this.props.match.params.id))
        const mealsArray = res.data.filter(({ meal_name: mealName}) => mealName === mealMatched[0].meal_name)
        this.setState({ mealsCategory: mealsArray })
      })
  }

  averageRating(ratings) {
    const averageRating = ratings.reduce((prev, curr) => prev + curr, 0) / ratings.length
    console.log('average', ratings.reduce((prev, curr) => prev + curr, 0))
    return averageRating
  }

  render() {
    console.log('mealsCategory: ', this.state.mealsCategory)
    return(
      <div className="container suggestions">
        <div className="columns is-multiline">
          {this.state.mealsCategory.map(meals =>
            <div key={meals.id} className="column is-one-third">
              <Link to={`/meals/${meals.id}/show`}>
                <div className="meal-image pink" style={{ backgroundImage: `url(${meals.meal_image})` }}>
                  <h1>{meals.restaurant_name}</h1>
                </div>
              </Link>
              <h2>{meals.restaurant_location}</h2>
              {meals.meal_price === null ? null : (
                <h2>{`Meal Price: £${meals.meal_price}`}</h2>
              )}
              <div className="stars">
                <p>Reader review</p>
                <ReactStars
                  className="star-container-index"
                  count={5}
                  value={this.averageRating(meals.ratings)}
                  size={24}
                  color2={'#ffe6e6'}
                  edit={false}
                />
                <p>{`(${meals.ratings.length})`}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default withRouter(MealCategory)
