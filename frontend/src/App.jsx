import './App.css';
import Navbar from './components/Navbar';
import Card from './components/Card';
import Footer from './components/Footer';
import AudioPlayer from './components/AudioPlayer';
import YTSearch from './components/YTSearch';

function App() {
  return (
    <>
      <Navbar />
      <YTSearch />
      <Footer />
    </>
  );
}

export default App;