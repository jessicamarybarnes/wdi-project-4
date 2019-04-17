import React from 'react'
import axios from 'axios'

import MealsForm from './meals-form'

class MealsEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: {} }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/meals/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err.message))
  }

  handleChange({ target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()
    const { ratings, creator, ...rest } = this.state.data
    axios.put(`/api/meals/${this.props.match.params.id}`, {
      ...rest
    })
      .then(() => this.props.history.push(`/meals/${this.props.match.params.id}/show`))
      .catch(err => console.log(err.message, ratings, creator))
  }

  handleCancel(e) {
    e.preventDefault()
    this.props.history.push(`/meals/${this.props.match.params.id}/show`)
  }

  render() {
    return (
      <main className="section">
        <div className="container">
          <MealsForm
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
            data={this.state.data}
          />
        </div>
      </main>
    )
  }
}

export default MealsEdit
