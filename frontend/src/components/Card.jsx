import React from 'react';

const Card = ({ title, description, inputPlaceholder }) => {
  return (
    <div className="w-full overflow-hidden shadow-lg bg-indigo-400 text-white">
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{title}</div>
        <p className="text-indigo-100 text-base">
          {description}
        </p>
      </div>
      <div className="px-6 py-4">
        <div className="flex items-center">
          <input
            type="text"
            placeholder={inputPlaceholder || "Enter your input"}
            className="w-full p-2 rounded-l text-indigo-600"
          />
          <button
            className="bg-indigo-600 text-white p-2 rounded-r hover:bg-indigo-500"
            onClick={() => alert('Search button clicked!')}
          >
            Search
          </button>
        </div>
      </div>
    </div>
  );
};

export default Card;