import React , { Component } from 'react';
import './App.css';
import Table from './Table.js';
import Form from './Form.js'

class App extends Component {
  state = {
    wanted_diamond: [],
    sale_diamonds: [
      {
        shape: 'Round',
        price: '$200',
        carat: '0.30',
        cut: 'Very Good',
        color: 'K',
        clarity: 'SI2',
        link: 'https://www.google.com',
      }
    ],
  }

  handleSubmit = wanted_diamond => {
    this.setState({ wanted_diamond: wanted_diamond })
  }

  render() {
    const sale_diamonds = this.state.sale_diamonds

    return (
    <div className='container'>
    <Form handleSubmit={this.handleSubmit}/>
    <Table diamondData={sale_diamonds} />
    </div>
    )
  }
}

export default App;
