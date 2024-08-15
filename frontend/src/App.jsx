import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar'
import Card from './components/Card'
import Footer from './components/Footer'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar />
      <Card
        title="Card Title"
        description="This is a description of the card content. It gives a brief overview of the topic."
        link="#"
        inputPlaceholder="Type something here..."
      />
      <Footer />
    </>
  )
}

export default App
