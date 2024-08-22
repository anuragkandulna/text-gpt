import "./App.css";
import Navbar from "./components/Navbar";
import Card from "./components/Card";
import Footer from "./components/Footer";
import AudioPlayer from "./components/AudioPlayer";
import YTSearch from "./components/YTSearch";
import ProductFeatures from "./components/ProductFeatures";
import UserRegistration from "./components/UserRegistration";

function App() {
    return (
        <>
            <Navbar />
            {/* <YTSearch /> */}
            <ProductFeatures />
            {/* <UserRegistration /> */}
            <Footer />
        </>
    );
}

export default App;
