import React, { Component } from 'react'

const TableHeader = () => {
  return (
    <thead>
      <tr>
        <th>Shape</th>
        <th>Price</th>
        <th>Carat</th>
        <th>Cut</th>
        <th>Color</th>
        <th>Clarity</th>
        <th>Link</th>
      </tr>
    </thead>
  )
}

const TableBody = props => {
  const rows = props.diamondData.map((row,index) => {
    return (
      <tr key={index}>
        <td>{row.shape}</td>
        <td>{row.price}</td>
        <td>{row.carat}</td>
        <td>{row.cut}</td>
        <td>{row.color}</td>
        <td>{row.clarity}</td>
        <td>
          <a href={row.link}>Link</a>
        </td>
      </tr>
    )
  })
  return <tbody>{rows}</tbody>
}

class Table extends Component {
  render() {
    const { diamondData } = this.props
    return (
      <table>
        <TableHeader />
        <TableBody diamondData={diamondData}/>
      </table>
    )
  }
}

export default Table
