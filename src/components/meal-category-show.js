import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import ReactStars from 'react-stars'


class MealCategoryShow extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      meal: [],
      ratings: [],
      averageRating: 0,
      accepted: null,
      rateThis: false
    }

    this.getMealShow = this.getMealShow.bind(this)
    this.averageRating = this.averageRating.bind(this)
    this.ratingChanged = this.ratingChanged.bind(this)
    this.handleDelete = this.handleDelete.bind(this)
    this.popUp = this.popUp.bind(this)
  }

  componentDidMount() {
    this.getMealShow()
  }

  getMealShow() {
    axios.get(`/api/meals/${this.props.match.params.id}`)
      .then(res => this.setState({ meal: res.data, ratings: res.data.ratings })
      )
      .then(() => this.averageRating())
  }

  averageRating() {
    const averageRating = this.state.ratings.reduce((prev, curr) => prev + curr, 0) / this.state.ratings.length
    console.log('average', this.state.ratings.reduce((prev, curr) => prev + curr, 0) / this.state.ratings.length)
    this.setState({ averageRating: averageRating })
  }

  ratingChanged(value) {
    console.log('rating changed', value)
    axios.post(`/api/meals/${this.props.match.params.id}/rating`, {
      rating: value
    })
      .then(() => this.getMealShow())
      .then(() => this.setState({ accepted: 'accepted' }))
  }

  handleDelete() {
    axios.delete(`/api/meals/${this.props.match.params.id}`)
      .then(() => this.props.history.push('/'))
      .catch(err => console.log(err.message))
  }

  popUp() {
    this.setState({ rateThis: true })
  }

  render() {
    console.log('meal is ', this.state.meal.restaurant_name)
    return(
      <div>
        <div className="meal-hero" style={{ backgroundImage: `url(${this.state.meal.meal_image})` }}>
          <h1 className="title title-over-image" >{this.state.meal.restaurant_name} , {this.state.meal.restaurant_location}
            <div className="icons">
              <Link to={`/meals/${this.props.match.params.id}/edit`}><i className="fas fa-edit"></i></Link>
              <Link to="#" onClick={this.handleDelete}><i className="fas fa-trash"></i></Link>
            </div>
          </h1>
          <div className="over-image">
            {this.state.meal.meal_price === null ? null : (
              <p>{`Meal Price: £${this.state.meal.meal_price}`}</p>
            )}
            {this.state.meal.more_info === null ? null : (
              <p>{this.state.meal.more_info}</p>
            )}
            <div className="stars">
              <p><b>Taste: </b></p>
              <ReactStars
                className="star-container"
                count={5}
                value={this.state.meal.taste_rating}
                size={24}
                color2={'#ffe6e6'}
                edit={false}
              />
            </div>
            <div className="stars">
              <p><b>Experience: </b></p>
              <ReactStars
                className="star-container"
                count={5}
                value={this.state.meal.experience_rating}
                size={24}
                color2={'#ffe6e6'}
                edit={false}
              />
            </div>
            <div className="stars">
              <p><b>Reader's review: </b></p>
              <ReactStars
                className="star-container"
                count={5}
                value={this.state.averageRating}
                size={24}
                color2={'#ffe6e6'}
                edit={false}
              />
              <p>( {this.state.ratings.length} )</p>
            </div>
            {this.state.meal.restaurant_link === null ? null : (
              <a href={this.state.meal.restaurant_link}><i className="fas fa-link"></i><span className="underline">Menu...</span></a>
            )}
            <br />
            <br />
            {this.state.rateThis === true ? null : (
              <Link to='#' className="rate underline" onClick={this.popUp}>Leave a review...</Link>
            )}
            {this.state.rateThis === false || this.state.accepted === 'accepted' ? null : (
              <div>
                <p><b>Rate the meal...</b></p>
                <ReactStars
                  count={5}
                  size={24}
                  color2={'#000000'}
                  edit={true}
                  onChange={this.ratingChanged}
                />
              </div>
            )}
          </div>
        </div>
      </div>
    )
  }
}

export default MealCategoryShow
