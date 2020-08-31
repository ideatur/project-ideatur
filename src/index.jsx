import * as $ from 'jquery'


import React from 'react'
import {render} from 'react-dom'
import './styles/styles.css'
import './styles/less.less'
import './styles/scss.scss'


const App = () => (
  <div className="container">
    <h1>Webpack works!</h1>
  </div>
)

render(<App/>, document.getElementById('app'))