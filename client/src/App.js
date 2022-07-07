import React, {useState, useEffect} from 'react'
import styles from './App.css'; 

function App() {

  

  return (
    <>
    <h1>Welcome to the Python Poker Program</h1>
    <div className={styles.row}>
    <div className={styles.column}>
    <Table/>
    </div>
    </div>
    <button>Load table</button>
    </>
  )
}

function Table() {
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
    <>
    <div>
      {(typeof table.cards === 'undefined') ? (
        <p>Error in database UwU</p>
      ):(
        <>
        <img className={styles.column}src='https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg'/>
        <img className={styles.column}src='https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg'/>
        <img className={styles.column}src='https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg'/>
        <img className={styles.column}src='https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg'/>
        <img className={styles.column}src='https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg'/>
        </>
      )
      }
    </div>
    </>
  )
}



export default App

///https://tekeye.uk/playing_cards/images/svg_playing_cards/backs/astronaut.svg
///(table.cards.map((card,i) => (
///  <img className='column' key={i} src={`https://tekeye.uk/playing_cards/images/svg_playing_cards/fronts/${card}.svg`}/>
///  )))