import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Browser, Route, Switch } from 'react-router-dom'
import './style.scss'

import NavBar from './components/nav'
import Home from './components/home'
import Suggestion from './components/suggestions'
import MealCategory from './components/meal-category'
import MealCategoryShow from './components/meal-category-show'
import MealsNew from './components/meals-new'
import MealsEdit from './components/meals-edit'

const App = () => {
  return(
    <Browser>
      <NavBar />
      <Home />
      <Switch>
        <Route exact path="/" component={Suggestion} />
        <Route exact path="/meals/new" component={MealsNew} />
        <Route exact path="/meals/:id" component={MealCategory} />
        <Route exact path="/meals/:id/edit" component={MealsEdit} />
        <Route exact path="/meals/:id/show" component={MealCategoryShow} />
      </Switch>
    </Browser>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root'))
