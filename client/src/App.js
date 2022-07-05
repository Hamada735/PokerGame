import React, {useState, useEffect} from 'react'

function App() {

  const [table,setTable] = useState([{}])

  useEffect(() => {
    fetch("/table").then(
      res => res.json()
    ).then(
      table => {
        setTable(table)
        console.log(table)
      }
    )
  },[]
  )

  return (
    
    <div>
      {(typeof table.cards === 'undefined') ? (
        <p>No cards dealt</p>
      ):(
        table.cards.map((card,i) => (
          <img className='column' key={i} src={`https://tekeye.uk/playing_cards/images/svg_playing_cards/fronts/${card}.svg`}/>
        ))
      )
      }

    </div>
  )
}

export default App

///https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg