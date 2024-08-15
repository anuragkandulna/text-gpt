import React from 'react';

const Card = ({ title, description, link, inputPlaceholder}) => {
  return (
    <div className="w-full overflow-hidden shadow-lg bg-blue-600 text-white">
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{title}</div>
        <p className="text-gray-200 text-base">
          {description}
        </p>
      </div>
        <div className="px-6 py-4">
            <input
            type="text"
            placeholder={inputPlaceholder || "Enter your input"}
            className="w-full p-2 rounded text-blue-600"
            />
        </div>
      <div className="px-6 pt-4 pb-2">
        <a
          href={link}
          className="inline-block bg-white text-blue-600 rounded-full px-3 py-1 text-sm font-semibold hover:bg-gray-200"
        >
          Learn More
        </a>
      </div>
    </div>
  );
};

export default Card;