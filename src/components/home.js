import React, {Fragment} from 'react'
import Link, { withRouter } from 'react-router-dom'


import Search from './search'

class Home extends React.Component {
  constructor() {
    super()
  }

  render() {
    const path = this.props.location.pathname.split('/').pop()
    console.log('path', path)
    if (path === 'show') {
      return null
    }
    return (
      <Fragment>
        <section className={`hero ${this.props.location.pathname === '/'? 'is-medium' : 'is-small' } is-dark is-bold`}>
          <div className="hero-body">
            <div className="container">
              <h1 className="title">
                What meal do you fancy?
              </h1>
              <Search />
            </div>
          </div>
        </section>
      </Fragment>
    )
  }
}

export default withRouter(Home)
