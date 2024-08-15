import './App.css';
import Navbar from './components/Navbar';
import Card from './components/Card';
import Footer from './components/Footer';
import AudioPlayer from './components/AudioPlayer';

function App() {
  return (
    <>
    <div className='w-full h-screen justify-between'>
      {/* <div id='navBarContainer'> */}
        <Navbar />
      {/* </div> */}
      <div id='cardContainer'>
        <Card
            title="Card Title"
            description="This is a description of the card content. It gives a brief overview of the topic."
            inputPlaceholder="Type something here..."
          />
      </div>
      <div id='audioPlayerContainer'
        className='p-4 flex-grow'>
        <AudioPlayer videoId="dQw4w9WgXcQ" />
      </div>
      <div id='footerContainer'
        className='fixed bottom-0 w-full'>
        <Footer />
      </div> 
    </div>

    </>
  );
}

export default App;