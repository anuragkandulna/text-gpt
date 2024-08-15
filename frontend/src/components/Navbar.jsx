import React, { useState } from 'react';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="bg-indigo-600 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold text-xl">
          MyApp
        </div>
        <div className="hidden md:flex space-x-4">
          <a href="#home" className="text-white hover:text-gray-200">Home</a>
          <a href="#about" className="text-white hover:text-gray-200">About</a>
          <a href="#services" className="text-white hover:text-gray-200">Services</a>
          <a href="#contact" className="text-white hover:text-gray-200">Contact</a>
        </div>
        <div className="md:hidden">
          <button
            onClick={toggleMenu}
            className="text-white focus:outline-none"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              {isOpen ? (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              ) : (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h16m-7 6h7"
                />
              )}
            </svg>
          </button>
        </div>
      </div>

      {isOpen && (
        <div className="md:hidden">
          <a href="#home" className="block text-white hover:text-gray-200 p-2">Home</a>
          <a href="#about" className="block text-white hover:text-gray-200 p-2">About</a>
          <a href="#services" className="block text-white hover:text-gray-200 p-2">Services</a>
          <a href="#contact" className="block text-white hover:text-gray-200 p-2">Contact</a>
        </div>
      )}
    </nav>
  );
};

export default Navbar;