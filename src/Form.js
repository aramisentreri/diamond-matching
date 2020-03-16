import React, { Component } from 'react'

class Form extends Component {
  initialState = {
    carat: '',
    cut: '',
    color: '',
    clarity: '',
  }
  state = this.initialState

  handleChange = event => {
    const { name, value } = event.target

    this.setState({
      [name]: value,
    })
  }

  submitForm = () => {
    this.props.handleSubmit(this.state)
    this.setState(this.initialState)
  }

  render() {
    const {carat, cut, color, clarity} = this.state;

    return (
      <form>
      <label htmlFor="carat">Carat</label>
      <input
        type="text"
        name="carat"
        id="carat"
        value={carat}
        onChange={this.handleChange} />
      <label htmlFor="cut">Cut</label>
      <input
        type="text"
        name="cut"
        id="cut"
        value={cut}
        onChange={this.handleChange} />
      <label htmlFor="color">Color</label>
      <input
        type="text"
        name="color"
        id="color"
        value={color}
        onChange={this.handleChange} />
      <label htmlFor="clarity">Clarity</label>
      <input
        type="text"
        name="clarity"
        id="clarity"
        value={clarity}
        onChange={this.handleChange} />

      <input type="button" value="Submit" onClick={this.submitForm} />
    </form>
    )
  }
}

export default Form;
